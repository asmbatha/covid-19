class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5438"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
