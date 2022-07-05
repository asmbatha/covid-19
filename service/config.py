class Config(object):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://ayanda:password@localhost/covid-19"
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:postgrespw@postgres:5432/covid-19"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
