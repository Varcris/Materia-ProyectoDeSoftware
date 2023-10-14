from flask import Blueprint
from flask import render_template
from src.core import auth
from src.web.helpers.auth import login_required

user_blueprint = Blueprint("users", __name__, url_prefix="/usuarios")


@user_blueprint.get("/")
@login_required
def index():
    users = auth.list_users()
    return render_template("users/index.html", users=users)
