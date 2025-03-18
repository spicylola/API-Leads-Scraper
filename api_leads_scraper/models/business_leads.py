from api_leads_scraper.app_init import db
from sqlalchemy.sql import func

class Businesses(db.Model):
    __tablename__ = 'businesses'

    place_id = db.Column(db.String, primary_key=True, unique=True, nullable=False)  # Unique Google Place ID
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    modified_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    display_name = db.Column(db.String, nullable=False)  # Name of the salon
    current_opening_hours = db.Column(db.Text, nullable=True)  # JSON or text of opening hours
    website_uri = db.Column(db.String, nullable=True)  # Salon website URL
    formatted_address = db.Column(db.String, nullable=False)  # Full address
    google_maps_uri = db.Column(db.String, nullable=False)  # Google Maps URL
    national_phone_number = db.Column(db.String, nullable=True)
    business_type = db.Column(db.String, nullable=False)