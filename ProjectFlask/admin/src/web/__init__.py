from flask import Flask, render_template
from src.web import error
from src.web.config import config  # <-- importamos la configuración
from src.core import database  # <-- importamos la base de datos
from src.web import routes  # <-- importamos las rutas
from src.web import commands  # <-- importamos los comandos


def create_app(
    env="development",  # <-- definimos el entorno de desarrollo
    static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
):
    app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación
    app.config.from_object(config[env])  # <-- setea la configuración
    database.init_app(app)  # <-- inicializamos la base de datos
    commands.register(app)  # <-- registramos los comandos
    routes.register(app)  # <-- registramos las rutas

    # ---- ejemplo de rutas ----

    @app.get("/")  # <-- forma nueva de agregar rutas
    def home():
        return render_template("home.html")  # <-- renderizamos el template home.html

    app.register_error_handler(
        404, error.not_found_error
    )  # <-- registramos el error 404

    def sarasa():
        return "sarasa"

    app.add_url_rule("/sarasa", view_func=sarasa)  # <-- forma antigua de agregar rutas

    return app
