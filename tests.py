from main import app
from web_requests import db
import json


print("###############    DB TESTS    ##################")
assert(len(db.getRaces()) == 21)

# TODO: Add more DB tests

print("###############  DB TESTS DONE ##################")


print("###############   API TESTS    ##################")

# TODO: Add API tests

print("############### API TESTS DONE ##################")

client = app.test_client()
def get_json(r):
   return json.loads(r.get_data().decode("utf-8"))