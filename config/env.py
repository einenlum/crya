from crya import BaseEnv


class Env(BaseEnv):
    APP_NAME: str
    DEBUG: bool = False
    DATABASE_URL: str


Env()
