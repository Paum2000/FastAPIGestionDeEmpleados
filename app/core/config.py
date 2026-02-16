from pydantic_settings import BaseSettings

class Config(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    db_type: str
    api_host: str
    debug: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"

config = Config()