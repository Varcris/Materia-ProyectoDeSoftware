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

    pass


class TestingConfig(Config):
    """Configuración de testing"""

    TESTING = True

    pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfing,
    "test": TestingConfig,
}
