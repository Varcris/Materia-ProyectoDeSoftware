from flask import Blueprint
from flask import render_template
from src.core import auth
from flask import abort
from src.web.helpers.auth import login_required
from src.web.helpers.auth import has_permission

user_blueprint = Blueprint("users", __name__, url_prefix="/usuarios")


@user_blueprint.get("/")
@login_required
def index():
    if not has_permission(["user_index"]):
        return abort(401)
    users = auth.list_users()
    return render_template("users/index.html", users=users)
