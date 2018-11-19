from main import app, db
import utils
from utils import makeId, getHash
import json


print("################    DB TESTS   ###################")
# Provided DB tests
## No buckets to begin with




print("################ DB TESTS DONE ###################")
# Provided API tests
print("################   API TESTS   ###################")

# ADD YOUR API TESTS HERE

client = app.test_client()
def get_json(r):
   return json.loads(r.get_data().decode("utf-8"))

