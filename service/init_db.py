from service import db

from service.models.global_cases import init_global_cases

db.create_all()

init_global_cases()
