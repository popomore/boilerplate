from enum import Enum


class ServerEnv(Enum):
    LOCAL = 'local'
    TEST = 'dev'
    PROD = 'prod'
