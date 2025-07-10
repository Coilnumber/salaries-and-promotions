import jwt
from datetime import datetime, timedelta
import bcrypt
from salaries_and_promotions.core.config import settings


# Создаём JWT на основании Payload, алгоритма и сикрет-ключа
def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
):
    now = datetime.utcnow()
    expires = now + timedelta(minutes=expire_minutes)

    to_encode = payload.copy()

    to_encode.update(
        exp=expires,
    )

    encoded_jwt = jwt.encode(to_encode,
                private_key,
                algorithm=algorithm)
    return encoded_jwt


# Декодируем JWT при помщи публичного ключа, т.е. получаем данные о пользователе, которые лежат в payload,
# который закодирован в JWT
def decode_jwt(
        token: str,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm ,):
    decoded_jwt = jwt.decode(token,
                             public_key,
                             algorithms= [algorithm])
    return decoded_jwt



# Хэшируем пароль при помощи библиотеки bcrypt
def hash_password(
        password: str,
):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt)
    return password_hash

## Cверяем введённый пароль с тем, что захэшированный лежит в БД
def validate_password(
        password: str,
        password_hash: bytes
)->bool:
    result = bcrypt.checkpw(password.encode(),
                            password_hash)
    return result

