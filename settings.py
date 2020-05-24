import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Funbox test app"
    test_env = os.getenv('TEST_ENV') == 'True'
