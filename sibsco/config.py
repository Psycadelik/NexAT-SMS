import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_KEY = 'Something secret'

    # SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') -- for PostgreSQL or MySql
    SQL_ALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cheza.db')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    DEBUG = False


configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
