from src.core import database  # <-- importamos la base de datos
from src.core import seeds


def register(app):
    @app.cli.command(name="resetdb")  # <-- comando para resetear la base de datos
    def reset_db():
        database.reset_db()

    @app.cli.command(name="seedsdb")  # <-- comando para resetear la base de datos
    def init_db():
        seeds.init_db()
