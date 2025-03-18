import logging
import click
import datetime
# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_apscheduler import APScheduler

from api_leads_scraper.app_init import create_app
# Create the app instance
app = create_app()
@app.cli.command('make_csv')
@click.option('--text_queries', required=True, help='Comma-separated list of search queries, e.g., "yoga studio, yoga classes, yoga"')
@click.option('--business_type', required=True, help='Type of business to search for, e.g., "yoga"')
def export_csv(text_queries, business_type):
    # This is to avoid circular imports, please dont freak out
    from api_leads_scraper.jobs.leads_job import export_businesses_to_csv
    from api_leads_scraper.jobs.google_map_job import populate_businesses
    if text_queries is None or business_type is None:
        raise Exception("Please Enter a text query or busness_type")

    # Convert text_queries string to a list
    queries_list = [query.strip() for query in text_queries.split(",")]
    current_time = datetime.datetime.utcnow()
    safe_filename = current_time.strftime('%Y-%m-%d_%H-%M') + ".csv"

    populate_businesses(text_queries, business_type)
    #export_businesses_to_csv(csv_filename=safe_filename, business_type=business_type)
    click.echo(f"Exported CSV for business type: {business_type} with queries: {queries_list}")



if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)

