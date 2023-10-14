from src.web.controllers.issues import issue_bp  # <-- importamos el blueprint issues
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.users import user_blueprint


def register(app):
    app.register_blueprint(issue_bp)  # <-- registramos el blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
