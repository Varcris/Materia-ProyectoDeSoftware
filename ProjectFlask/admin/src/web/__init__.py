from flask import Flask, render_template
from src.web import error
from src.web.controllers import issues  # <-- importamos el blueprint issues
from src.web.config import config  # <-- importamos la configuración
from src.core import database  # <-- importamos la base de datos
from src.core import seeds  # <-- importamos los seeds


def create_app(
    env="development",  # <-- definimos el entorno de desarrollo
    static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
):
    app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación
    app.config.from_object(config[env])  # <-- setea la configuración

    database.init_app(app)  # <-- inicializamos la base de datos

    app.register_blueprint(issues.issue_bp)  # <-- registramos el blueprint

    @app.get("/")  # <-- forma nueva de agregar rutas
    def home():
        return render_template("home.html")  # <-- renderizamos el template home.html

    app.register_error_handler(
        404, error.not_found_error
    )  # <-- registramos el error 404

    @app.cli.command(name="reset_db")  # <-- comando para resetear la base de datos
    def reset_db():
        database.reset_db()

    @app.cli.command(name="seeds_db")  # <-- comando para resetear la base de datos
    def seeds_db():
        seeds.run()

    def sarasa():
        return "sarasa"

    app.add_url_rule("/sarasa", view_func=sarasa)  # <-- forma antigua de agregar rutas

    return app
