from database import DevDatabase, ProdDatabase


class DevSettings(DevDatabase):
    ENV = 'development'
    SERVER_NAME = "127.0.0.1:8000"
    DEBUG = True
    SECRET_KEY = 'ADs1JKJ2=A-=-140*&'
    SESSION_COOKIE_NAME = 'NOT SESSION'


class ProdSettings(ProdDatabase):
    ENV = 'production'
    SECRET_KEY = 'barSSS=A-=-ds11*&'
    SESSION_COOKIE_NAME = 'MD5_DATA'


settings = {
    'dev': DevSettings,
    'prod': ProdSettings,
    'default': DevSettings
}
