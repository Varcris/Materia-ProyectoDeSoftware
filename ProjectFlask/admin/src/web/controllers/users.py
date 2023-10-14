from flask import Blueprint
from flask import render_template
from flask import session
from flask import abort
from src.core import auth
from src.web.helpers.auth import is_authenticated

user_blueprint = Blueprint("users", __name__, url_prefix="/usuarios")


@user_blueprint.get("/")
def index():
    if not is_authenticated(session):
        return abort(401)
    users = auth.list_users()
    return render_template("users/index.html", users=users)
