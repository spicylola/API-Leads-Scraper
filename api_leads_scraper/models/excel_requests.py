from api_leads_scraper.app_init import db
from sqlalchemy.sql import func

class ExcelRequest(db.Model):
    __tablename__ = 'excel_requests'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID
    request_id = db.Column(db.String, unique=True, nullable=False)  # Unique identifier for the request
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key linking to User model
    status = db.Column(db.String, nullable=False, default='pending')  # Request status: pending, completed, or error #TODO: ENUM
    error_msg = db.Column(db.String, nullable=True)
    file_path = db.Column(db.Text, nullable=True)  # Path to the generated Excel file
    download_url = db.Column(db.Text, nullable=True)  # URL to download the generated file
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)  # Creation timestamp
    completed_at = db.Column(db.DateTime(timezone=True), nullable=True)  # Timestamp for when the request was completed

    # Relationship with the User model
    user = db.relationship("User", back_populates="requests")