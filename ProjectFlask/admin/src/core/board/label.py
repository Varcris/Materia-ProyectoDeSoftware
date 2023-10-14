from datetime import datetime

from src.core.database import db


class Label(db.Model):
    __tablename__ = "labels"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(100))
    # issues = db.relationship("Issue", back_populates="label")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)
