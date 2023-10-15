from src.web.controllers.issues import issue_bp
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.users import user_blueprint
from src.web.controllers.home import home_bp


def register(app):
    app.register_blueprint(issue_bp)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(home_bp)
