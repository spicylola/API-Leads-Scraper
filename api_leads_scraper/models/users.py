from api_leads_scraper.app_init import db
from sqlalchemy.sql import func  # Import func for timestamp defaults

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)  # User's email
    password_hash = db.Column(db.String, nullable=False)  # User's hashed password
    requests = db.relationship("ExcelRequest", back_populates="user")  # Relationship with ExcelRequest