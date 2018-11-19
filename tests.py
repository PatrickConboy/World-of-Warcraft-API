from main import app, db
import json

session = db.session

print("###############    DB TESTS    ##################")
# Testing to see if our data is in the data base and db methods work
assert(len(db.getRaces()) == 21)

# TODO: Add more DB tests

print("###############  DB TESTS DONE ##################")


print("###############   API TESTS    ##################")
client = app.test_client()
def get_json(r):
   return json.loads(r.get_data().decode("utf-8"))

print("Testing '/race' method...")
r = client.get('/race')
assert(r.status_code == 200)
contents = get_json(r)
assert("races" in contents)
r = client.get('/race' + 'wah')
assert(r.status_code == 404)

# TODO: Add API tests for '/race/<race>'

# TODO: Add more API tests

print("############### API TESTS DONE ##################")