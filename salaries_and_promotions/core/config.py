from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / 'salaries_and_promotions' / 'auth'/ 'certs' / 'private.pem'
    public_key_path: Path = BASE_DIR / 'salaries_and_promotions'/ 'auth'/ 'certs' / 'public.pem'
    algorithm: str = 'RS256'
    access_token_expire_minutes: int = 60




class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()