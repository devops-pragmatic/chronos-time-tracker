import os


def get_database_url():
    """
    Returns the database URL from environment variables.
    See: https://12factor.net/config
    """
    return os.environ.get("DATABASE_URL", "mysql+pymysql://root:password@db:3306/chronos")
