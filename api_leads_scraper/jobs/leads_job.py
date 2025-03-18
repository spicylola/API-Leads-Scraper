import pandas as pd
from api_leads_scraper.app_init import db
from api_leads_scraper.models import Businesses # Import your SQLAlchemy models



def export_businesses_to_csv(csv_filename="businesses.csv", business_type= None):
    """
    Exports nail salon data from the SQLite database to a CSV file.
    """
    from api_leads_scraper.app import app
    businesses = None
    with app.app_context():  # Ensures function runs inside Flask context
        if business_type == None:
            businesses = db.session.query(Businesses).all()
        else:
            businesses = db.session.query(Businesses).filter_by(business_type=business_type).all()

        data = [
            {
                "place_id": business.place_id,
                "display_name": business.display_name,
                "formatted_address": business.formatted_address,
                "national_phone_number": business.national_phone_number,
                "website_uri": business.website_uri,
                "google_maps_uri": business.google_maps_uri,
            }
            for business in businesses
        ]

        df = pd.DataFrame(data)
        df.to_csv(csv_filename, index=False)

        print(f"Exported {len(businesses)} records to {csv_filename}")

# Example usage
# export_nail_salons_to_csv("nail_salons.csv")
