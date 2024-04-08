from pydantic_settings import BaseSettings, SecretStr

try:
    config = BaseSettings(".env")
except FileNotFoundError:
    config = BaseSettings()

DATABASE_URL = config("DATABASE_URL", cast=SecretStr)

TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=SecretStr)
