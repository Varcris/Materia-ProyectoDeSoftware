""" Modulo de configuración de la aplicación """


class Config(object):
    """Base de configuración"""

    SECRET_KEY = "SECRET"
    TESTING = False
    SESSION_TYPE = "filesystem"


class ProductionConfing(Config):
    """Configuración de producción"""

    pass


class DevelopmentConfig(Config):
    """Configuración de desarrollo"""

    DB_USER = "postgres"
    DB_PASS = "admin"
    DB_HOST = "localhost"
    DB_NAME = "projectFlask"
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
