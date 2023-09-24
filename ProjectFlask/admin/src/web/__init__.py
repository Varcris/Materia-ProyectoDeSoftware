from flask import Flask, render_template
from src.web import error
from src.web.controllers import issues  # <-- importamos el blueprint issues


def create_app(
    env="development",  # <-- definimos el entorno de desarrollo
    static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
):
    app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación

    app.register_blueprint(issues.issue_bp)  # <-- registramos el blueprint

    @app.get("/")  # <-- forma nueva de agregar rutas
    def home():
        return render_template("home.html")  # <-- renderizamos el template home.html

    def sarasa():
        return "sarasa"

    app.add_url_rule("/sarasa", view_func=sarasa)  # <-- forma antigua de agregar rutas

    app.register_error_handler(
        404, error.not_found_error
    )  # <-- registramos el error 404
    return app
