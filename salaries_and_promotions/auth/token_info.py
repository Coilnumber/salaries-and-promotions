from pydantic import BaseModel

class TokenInfo(BaseModel):
    """ Схема для валидации токена """
    access_token: str
    token_type: str