from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__, url_prefix="/")  # <-- creamos el blueprint


@home_bp.get("/")  # <-- forma nueva de agregar rutas
def home():
    return render_template("home.html")  # <-- renderizamos el template home.html
