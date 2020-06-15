from decouple import config

class Config:
    SECRET_KEY = 'codigofacilito'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://freddy:soriano00@localhost/project_web_facilito'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME', default='correo@host.com')
    MAIL_PASSWORD = config('MAIL_PASSWORD', default='password123')

class TestConfig(Config):
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'mysql://fredy:soriano00:@localhost/project_web_facilito_test'
=======
    SQLALCHEMY_DATABASE_URI = 'mysql://freddy:soriano00@localhost/project_web_facilito_test'
>>>>>>> faa77e69ee8133cd7f7562a0a5870d5b17cff75c
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

class ProductionConfig(DevelopmentConfig):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
