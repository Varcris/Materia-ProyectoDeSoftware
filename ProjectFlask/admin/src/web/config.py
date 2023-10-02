""" Modulo de configuración de la aplicación """
from os import environ


class Config(object):
    """Base de configuración"""

    SECRET_KEY = "SECRET"
    TESTING = False
    SESSION_TYPE = "filesystem"


class ProductionConfing(Config):
    """Configuración de producción"""

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class DevelopmentConfig(Config):
    """Configuración de desarrollo"""

    print("DB_USER", environ.get("DB_USER"))
    print("DB_PASS", environ.get("DB_PASS"))
    print("DB_HOST", environ.get("DB_HOST"))
    print("DB_NAME", environ.get("DB_NAME"))

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )


class TestingConfig(Config):
    """Configuración de testing"""

    TESTING = True

    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfing,
    "test": TestingConfig,
}
