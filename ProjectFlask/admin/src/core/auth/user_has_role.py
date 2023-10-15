from src.core.database import db

user_has_role = db.Table(
    "user_has_role",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True),
    db.Column(
        "institution_id", db.Integer, db.ForeignKey("institution.id"), primary_key=True
    ),
)
