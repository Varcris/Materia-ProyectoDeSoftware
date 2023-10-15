import datetime
from src.core.database import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
    permissions = db.relationship("Permission", secondary=role_permissions)
    users = db.relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role {self.name}>"

    def __str__(self):
        return f"{self.name}"
