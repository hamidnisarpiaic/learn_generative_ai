from starlette.config import Config
from starlette.datastructures import Secret
import os

config = Config(".env")

DATABASE_URL = config('DATABASE_URL', cast=Secret)
