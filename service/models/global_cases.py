# Import the database object (db) from the main application module
from service import db
from sqlalchemy.dialects.postgresql import JSON
from service.models.base import Base


class GlobalCases(Base):
    __tablename__ = "global_cases"

    data = db.Column(JSON)

    # New instance instantiation procedure
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<GlobalCases %r>" % (self.data)


def addGlobalCase(input):
    db.session.add(GlobalCases(input))
    db.session.commit()


def getGlobalCase():
    global_case = GlobalCases.query.order_by(GlobalCases.id.desc()).first()

    return global_case.data
