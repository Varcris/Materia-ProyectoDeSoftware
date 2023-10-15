from functools import wraps
from flask import session
from flask import abort
from src.core.auth import find_user_by_email
from src.core.auth import list_permissions_by_user_id


def is_authenticated(session):
    return session.get("user") is not None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_authenticated(session):
            return abort(401)
        return f(*args, **kwargs)

    return decorated_function


def has_permission(required_permissions_list):
    has_permission = True
    user = find_user_by_email(session.get("user"))
    user_permissions_list = list_permissions_by_user_id(user.id)
    for permission in required_permissions_list:
        if permission not in user_permissions_list:
            print("has_permission === no esta el permiso %s" % permission)
            has_permission = False
            break
    return has_permission
