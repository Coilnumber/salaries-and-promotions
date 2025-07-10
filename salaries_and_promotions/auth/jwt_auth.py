import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer , HTTPAuthorizationCredentials, HTTPBearer
from . import utils as jwt_utils
from salaries_and_promotions.users.users_db import users_db
from .token_info import TokenInfo
from salaries_and_promotions.users.schemas import UserSchema
from salaries_and_promotions.core.config import settings

from fastapi import Depends, APIRouter, status, HTTPException, Form

router = APIRouter(prefix="/auth", tags=["auth"])

#http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')



# Сперва находим пользователя по логину, если найден по паролю
def validate_auth_user(
        username: str = Form(),
        password: str = Form(...),
):
    exception_unauth = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Введите заново логин или пароль",
    )

    if not (user:= users_db.get(username)):
        raise exception_unauth

    if not jwt_utils.validate_password(password = password,
                                       password_hash=user.password):
        raise exception_unauth
    return user


# Логинимся и возвращаем токен пользователю
@router.post("/login", response_model=TokenInfo)
def auth_user_token_issue(
        user: UserSchema = Depends(validate_auth_user),
):
    payload = {
        'sub': user.login,
        'login': user.login,
    }
    token = jwt_utils.encode_jwt(payload=payload)
    return TokenInfo(access_token=token,
                     token_type="Bearer",)



# Подписываем приватный ключ и получаем конкретного пользователя
def current_user(
        #credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
        token: str = Depends(oauth2_scheme),
):
    #token = credentials.credentials
    try:
        payload = jwt_utils.decode_jwt(token=token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token error",
        )

    login:str = payload.get("sub")

    if user:= users_db.get(login):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Данные некорректы",
        )


# Проверяем статус пользователя
def current_active_user(
        user: UserSchema = Depends(current_user),
):
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive or deleted",
        )
    return user


# Выдаём нужные нам данные в зависимости от статуса пользователя и подписания  секретного ключа
@router.get("/users/get_data")
def current_auth_user_data(
        user: UserSchema = Depends(current_active_user),
):
    return {
        'name': user.name,
        'Salary': user.salary,
        'DateOfPromotion': user.date_of_promotion,
    }

