from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# from service.models.global_cases import GlobalCases

app = Flask(__name__)
app.config.from_object(Config)

# print("SQLALCHEMY_DATABASE_URI", Config.SQLALCHEMY_DATABASE_URI)

db = SQLAlchemy(app)

# db.create_engine(Config.SQLALCHEMY_DATABASE_URI)

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
    app.run(host="0.0.0.0", debug=True)
