from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    """Inicialización de la base de datos.

    Args:
        app (Flask): Aplicación Flask
    """

    db.init_app(app)
    config_db(app)


def config_db(app):
    """Configuración de la base de datos.

    Args:
        app (Flask): Aplicación Flask
    """

    @app.teardown_request  # <-- decorador para ejecutar la función luego de cada request
    def close_session(exeption=None):
        """Cierre de la sesión de la base de datos."""
        db.session.close()


def reset_db():
    print("🗑️ Eliminando base de datos...")
    db.drop_all()
    print("🛠️ Creando base de datos...")
    db.create_all()
    print("✅ Base de datos creada!")
