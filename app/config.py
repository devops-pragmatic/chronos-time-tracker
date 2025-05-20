import os


def get_database_url():
    """
    Get the database URL from environment variables or use a default SQLite database for local development.
    For Docker Compose, set DATABASE_URL to point to MySQL.
    """
    return os.getenv("DATABASE_URL", "sqlite:///app.db")
