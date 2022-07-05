from typing_extensions import Self
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# from service.models.global_cases import GlobalCases

app = Flask(__name__)
app.config.from_object(Config)

engine = SQLAlchemy.create_engine(
    self=Self,
    sa_url=Config.SQLALCHEMY_DATABASE_URI,
    engine_opts={},
)

try:
    with engine.connect() as conn:
        conn.execute("commit")
        # Do not substitute user-supplied database names here.
        conn.execute('CREATE DATABASE "covid-19"')
except:
    print("database already created")

db = SQLAlchemy(app)

import init_db

from models.global_cases import getGlobalCase


# Sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return {"error", 404}


@app.route("/global_cases", methods=["GET"])
def hello():
    return getGlobalCase()


if __name__ == "__main__":
    app.run()
