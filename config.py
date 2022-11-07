"""
Configuration class file
"""


class LocalConfig:
    """
    SQLAlchemy config
    """
    # Database option
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
