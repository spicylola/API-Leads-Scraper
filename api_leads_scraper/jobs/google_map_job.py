from api_leads_scraper.service.google_maps_service import get_places, get_place_details
from api_leads_scraper.models.business_leads import Businesses

# TODO: Evolve this to be more dynamic
#text_queries = ["nail salon in new york city", "nail salon nyc", "nail salon manhattan", "nail salon harlem ny", "nail salon staten island", "beauty and spa new york city"]


def populate_businesses(text_queries, business_type):
    """
    Fetch places and populate the nail_salons database table.
    """
    from api_leads_scraper.app_init import db
    from api_leads_scraper.app import app
    # Store all place IDs from the queries
    with app.app_context():  # Ensure app context is active
        # Store all place IDs from the queries
        places_ids = []
        for query in text_queries:
            places = get_places(query)  # Call your service to fetch places
            places_ids.extend(places)

        # Iterate over place IDs to fetch details and populate the database
        idx = 1
        for place_id in places_ids:
            place_info = get_place_details(place_id)
            name = place_info.get("displayName").get("text")
            #cur_hours = str(place_info.get("currentOpeningHours"))
            website = place_info.get("websiteUri")
            address = place_info.get("formattedAddress")
            maps_uri = place_info.get("googleMapsUri")
            phone = place_info.get("nationalPhoneNumber")
            place_id = place_info.get("id")

            # Check for duplicates before adding to the database
            if not db.session.query(Businesses).filter_by(place_id=place_id).first():
                new_business = Businesses(
                    place_id=place_id,
                    display_name=name,
                    formatted_address=address,
                    national_phone_number=phone,
                    website_uri=website,
                    google_maps_uri=maps_uri,
                    business_type = business_type
                )
                db.session.add(new_business)
            if idx == 100:
                break
            print(f"Processed {idx} out of {len(places_ids)}")
            idx +=1

        # Commit the changes
        db.session.commit()
        print(f"Populated {idx} new businesses with {business_type} into the database.")