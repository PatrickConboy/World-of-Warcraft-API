from main import app, db
import json

session = db.session

print("###############    DB TESTS    ##################")
# Testing to see if our data is in the data base and db methods work
assert(len(db.getRaces()) == 21)

# TODO: Add more in depth DB tests

print("###############  DB TESTS DONE ##################")


print("###############   API TESTS    ##################")
client = app.test_client()
def get_json(r):
   return json.loads(r.get_data().decode("utf-8"))

base_url = 'http://127.0.0.1:5000'

print("Testing '/race' method...")
r = client.get('/race')
assert(r.status_code == 200)
contents = get_json(r)
assert("races" in contents)
r = client.get('/race' + 'wah')
assert(r.status_code == 404)

# Testing a GET on race/Human
print("Testing '/race/<raceName>' method...")
r = client.get(base_url + '/race/Human')
contents = get_json(r)
assert(contents['name'] == 'Human')
assert(contents['link'] == '/race/Human')
assert(contents['description'] == 'test')
assert(contents['faction'] == 'alliance')

# Testing a GET on race/Troll
r = client.get(base_url + '/race/Troll')
contents = get_json(r)
assert(contents['name'] == 'Troll')
assert(contents['link'] == '/race/Troll')
assert(contents['description'] == 'test')
assert(contents['faction'] == 'horde')

# TODO: Add API tests for any new methods we implement

# TODO: Add more in depth API tests

print("############### API TESTS DONE ##################")