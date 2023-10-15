import datetime
from src.core.database import db


class Permission(db.Model):
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    roles = db.relationship("Role", secondary=role_permissions)

    def __repr__(self):
        return f"<Permission {self.name}>"

    def __str__(self):
        return f"{self.name}"
