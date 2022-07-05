import requests
import json
from service import db

from service.models.global_cases import addGlobalCase

db.create_all()


def get_global_cases():
    url = "https://covid-api.mmediagroup.fr/v1//cases?country=Global"
    req = requests.get(url)
    data = req.content
    json_data = json.loads(data)
    return json_data["All"]


data = get_global_cases()

print("addGlobalCase", data)

addGlobalCase(data)
