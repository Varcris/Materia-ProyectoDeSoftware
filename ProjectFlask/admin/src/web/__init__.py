# from flask import Flask  # <-- importamos Flask desde el paquete flask
# from flask import (
#     render_template,
# )  # <-- importamos render_template desde el paquete flask
# from src.web import error


# def create_app(
#     env="development",  # <-- definimos el entorno de desarrollo
#     static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
# ):  # <-- función que crea la aplicación
#     app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación

#     @app.get("/")  # <-- forma nueva de agregar rutas
#     def home():
#         return render_template("home.html")  # <-- renderizamos el template home.html

#     def sarasa():
#         return "sarasa"

#     app.add_url_rule("/sarasa", view_func=sarasa)  # <-- forma antigua de agregar rutas

#     app.register_error_handler(
#         404, error.not_found_error
#     )  # <-- registramos el error 404
#     return app
from src.web import error
from flask import Flask, flash, redirect, render_template, request, url_for


def create_app(
    env="development",  # <-- definimos el entorno de desarrollo
    static_folder="../../static",  # <-- definimos la carpeta de archivos estáticos
):  # <-- función que crea la aplicación
    app = Flask(__name__, static_folder=static_folder)  # <-- crea la aplicación
    app.secret_key = "12345678"

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        error = None
        if request.method == "POST":
            if (
                request.form["username"] != "admin"
                or request.form["password"] != "secret"
            ):
                flash("Invalid password provided", "error")
            else:
                flash("You were successfully logged in", "success")
                return redirect(url_for("index"))
        return render_template("login.html", error=error)

    return app
