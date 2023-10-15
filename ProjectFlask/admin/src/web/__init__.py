from flask import Flask  # <-- importamos la clase Flask
from flask import (
    render_template,
)  # <-- importamos la función render_template para renderizar templates
from flask_session import Session  # <-- importamos la clase Session de flask_session
from src.web import error  # <-- importamos el módulo de errores
from src.web.config import config  # <-- importamos la configuración
from src.core import database  # <-- importamos la base de datos
from src.web import routes  # <-- importamos las rutas
from src.web import commands  # <-- importamos los comandos
from src.web.helpers import auth  # <-- importamos el módulo de autenticación
import logging  # <-- importamos el módulo de logging que viene con python para ver los logs

logging.basicConfig()  # <-- inicializamos el logging
logging.getLogger("sqlalchemy.engine").setLevel(
    logging.DEBUG
)  # <-- seteamos el nivel de logging para sqlalchemy
session = Session()  # <-- inicializamos la sesión de flask_session


def create_app(
    env="development",  # <-- definimos el entorno de desarrollo
    static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
):
    """Crea la aplicación de flask"""
    app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación
    app.config.from_object(config[env])  # <-- setea la configuración
    session.init_app(app)  # <-- inicializamos la sesión de flask_session
    database.init_app(app)  # <-- inicializamos la base de datos
    commands.register(app)  # <-- registramos los comandos
    routes.register(app)  # <-- registramos las rutas
    # ---- ejemplo de rutas ----

    app.register_error_handler(
        404, error.not_found_error
    )  # <-- registramos el error 404
    app.register_error_handler(
        401, error.unauthorized_error
    )  # <-- registramos el error 401

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    def sarasa():
        return "sarasa"

    app.add_url_rule("/sarasa", view_func=sarasa)  # <-- forma antigua de agregar rutas

    return app
