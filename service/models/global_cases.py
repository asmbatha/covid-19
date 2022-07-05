# Import the database object (db) from the main application module
from main import db
from sqlalchemy.dialects.postgresql import JSON
from models.base import Base
import json
import requests


class GlobalCases(Base):
    __tablename__ = "global_cases"

    data = db.Column(JSON)

    # New instance instantiation procedure
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<GlobalCases %r>" % (self.data)


globalCaseSchema = {
    "type": "object",
    "properties": {
        "confirmed": {"type": "number"},
        "deaths": {"type": "number"},
        "population": {"type": "number"},
    },
    "required": ["confirmed", "deaths", "population"],
}


def init_global_cases():
    url = "https://covid-api.mmediagroup.fr/v1//cases?country=Global"
    req = requests.get(url)
    data = req.content
    json_data = json.loads(data)["All"]

    if "population" in json_data and "confirmed" in json_data and "deaths" in json_data:
        addGlobalCase(json_data)
    else:
        print("invalid global_cases")


def addGlobalCase(input):
    db.session.add(GlobalCases(input))
    db.session.commit()


def getGlobalCase():
    global_case = GlobalCases.query.order_by(GlobalCases.id.desc()).first()

    return global_case.data
