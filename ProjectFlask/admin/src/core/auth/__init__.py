from core.auth.user import User
from src.core.database import db
from src.core.bcrypt import bcrypt


def list_users():
    """Lista todos los usuarios"""
    return User.query.all()


def create_user(**kwargs):
    """Crear un usuario y hashea la contraseña en la base de datos"""
    hash = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    kwargs.update(password=hash.decode("utf-8"))
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email(email):
    """Busca y devuelve un usuario por su email"""
    return User.query.filter_by(email=email).first()


def check_user(email, password):
    """Chequea si el usuario existe y si la contraseña es correcta, devuelve el usuario o None"""
    user = find_user_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password.encode("utf-8")):
        return user
    else:
        return None


def list_permissions_by_user_id(user_id):
    """Devuelve una lista de permisos de un usuario por su id"""
    user = User.query.get(user_id)
    permissions = []
    for role in user.roles:
        for permission in role.permissions:
            permissions.append(permission.name)
    return permissions
