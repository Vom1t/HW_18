# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}