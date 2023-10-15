import datetime
from src.core.database import db


class Institution(db.Model):
    __tablename__ = "institutions"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
