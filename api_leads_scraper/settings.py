import os

# Flask App Configurations
class Config:
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///business.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Suppress warnings for performance optimization

    # Debugging Mode
    DEBUG = os.getenv('DEBUG', True)

    # Uploads Directory (for Excel file storage)
    #UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')

    # Pagination (optional for APIs that return large datasets)
    ITEMS_PER_PAGE = int(os.getenv('ITEMS_PER_PAGE', 10))
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    SCHEDULER_API_ENABLED = True

# Development Configurations
class DevelopmentConfig(Config):
    DEBUG = True

# Production Configurations
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///production.db')

# Configuration Mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
