from logging import config as logging_config
from pathlib import Path

from pydantic_settings import BaseSettings

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


BASE_DIR = PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """Главный класс настроек всего приложения"""

    project_name: str = "notification_service"
    secret_key: str = ""
    app_port: int = 8000

    rabbit_host: str = "127.0.0.1"
    rabbit_port: int = 5672
    rabbit_user: str = "guest"
    rabbit_password: str = "guest"

    class Config:
        env_file = BASE_DIR/'.env'
        extra = 'ignore'


settings = Settings()
