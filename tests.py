from main import app, db
import json

session = db.session

print("###############    DB TESTS    ##################")
# Testing to see if our data is in the data base and db methods work
print("   Testing Race methods...")
assert(len(db.getRaces()) == 21)

print("   Testing Class methods...")
assert(len(db.getClasses()) == 12)

print("   Testing Battlegroup methods...")
assert(len(db.getBattlegroups()) == 9)

# TODO: Add more in depth DB tests

print("###############  DB TESTS DONE ##################")


print("###############   API TESTS    ##################")
client = app.test_client()
def get_json(r):
   return json.loads(r.get_data().decode("utf-8"))

base_url = 'http://127.0.0.1:5000'

# Testing a GET on /race
print("   Testing '/race' path...")
r = client.get('/race' + 'wah')
assert(r.status_code == 404)
r = client.get('/race')
assert(r.status_code == 200)
contents = get_json(r)
assert("races" in contents)
assert(len(contents["races"]) == 21)
assert(contents["races"][0]["name"] == "Human")
assert(contents["races"][0]["faction"] == "alliance")

# Testing a GET on /race/Human
print("   Testing '/race/<raceName>' path...")
r = client.get(base_url + '/race/Human')
contents = get_json(r)
assert(contents['name'] == 'Human')
assert(contents['link'] == '/race/Human')
assert(contents['description'] == 'test')
assert(contents['faction'] == 'alliance')

# Testing a GET on /race/Troll
r = client.get(base_url + '/race/Troll')
contents = get_json(r)
assert(contents['name'] == 'Troll')
assert(contents['link'] == '/race/Troll')
assert(contents['description'] == 'test')
assert(contents['faction'] == 'horde')

# Testing a GET on /class
print("   Testing '/class' path...") 
r = client.get('/class' + 'wah')
assert(r.status_code == 404)
r = client.get('/class')
assert(r.status_code == 200)
contents = get_json(r)
assert("classes" in contents)
assert(len(contents["classes"]) == 12)
assert(contents["classes"][0]["class name"] == "Warrior")

# Testing a GET on /class/Warrior
print("   Testing '/class/<className>' path...")
r = client.get(base_url + '/class/Warrior')
contents = get_json(r)
assert(contents['class name'] == 'Warrior')
assert(contents['link'] == '/class/Warrior')
assert(contents['power type'] == 'rage')

# Testing a GET on /class/Death Knight
r = client.get(base_url + '/class/Death Knight')
contents = get_json(r)
assert(contents['class name'] == 'Death Knight')
assert(contents['link'] == '/class/Death%20Knight')
assert(contents['power type'] == 'runic-power')

# Testing a GET on /battlegroup
print("   Testing '/battlegroup' path...")
r = client.get('/battlegroup')
assert(r.status_code == 200)
contents = get_json(r)
assert("battlegroups" in contents)
assert(len(contents["battlegroups"]) == 9)


# TODO: Add API tests for any new methods we implement

# TODO: Add more in depth API tests

print("############### API TESTS DONE ##################")