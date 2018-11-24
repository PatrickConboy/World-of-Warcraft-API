from main import app, db
import json

session = db.session

print("###############    DB TESTS    ##################")
# Testing to see if our data is in the data base and db methods work
print("   Testing Race methods...")
assert(len(db.getRaces()) == 19)
race = db.getRace("Goblin")
assert(race is not None)
assert(db.getRaces()[8] is race)
db.addRace(name="Wizard", id = 20, faction = "Alliance", playableClass = "Hunter", description = "Od" )
assert(len(db.getRaces()) == 20)
wizard = db.getRace("Wizard")
assert(wizard is not None)
assert(db.getRaces()[19] is wizard)
db.commit()
db.deleteRace(wizard)
wizard = db.getRace("Wizard")
assert(wizard is None)
db.commit()
assert(len(db.getRaces()) == 19)


print("   Testing Class methods...")
assert(len(db.getClasses()) == 12)
class1 = db.getClass("Priest")
assert(class1 is not None)
assert(db.getClasses()[4] is class1)
db.addClass(name="Pirate", powerType = "fury", roles = "Tank")
assert(len(db.getClasses()) == 13)
class2 = db.getClass("Pirate")
assert(class2 is not None)
assert(db.getClasses()[12] is class2)
db.commit()
db.deleteClass(class2)
class2 = db.getClass("Pirate")
assert(class2 is None)
db.commit()
assert(len(db.getClasses()) == 12)


print("   Testing Faction methods...")
assert(len(db.getFactions()) == 2)
alliance = db.getFaction("Alliance")
assert(alliance is not None)
assert(db.getFactions()[0] is alliance)
db.addFaction(name="Neutral", description = "Od")
assert(len(db.getFactions()) == 3)
neutral = db.getFaction("Neutral")
assert(neutral is not None)
assert(db.getFactions()[2] is neutral)
db.commit()
db.deleteFaction(neutral)
neutral = db.getFaction("Neutral")
assert(neutral is None)
db.commit()
assert(len(db.getFactions()) == 2)


print("   Testing Role methods...")
assert(len(db.getRoles()) == 3)

print("   Testing Battlegroup methods...")
assert(len(db.getBattlegroups()) == 9)

print("   Testing ArenaStat methods...")
assert(len(db.getStats()) == 4)

print("###############  DB TESTS DONE ##################")

print(" ")

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
assert(len(contents["races"]) == 19)
assert(contents["races"][0]["name"] == "Human")

# Testing a GET on /race/Human
print("   Testing '/race/<raceName>' path...")
r = client.get(base_url + '/race/Human')
assert(r.status_code == 200)
contents = get_json(r)
assert(contents['name'] == 'Human')
assert(contents['link'] == '/race/Human')
assert(contents['faction'] == 'alliance')
assert(contents['playableClass'] == 'Hunter, Mage, Paladin, Priest, Rogue, Warlock, Warrior, Death Knight, Monk')

# Testing a GET on /race/Troll
r = client.get(base_url + '/race/Troll')
assert(r.status_code == 200)
contents = get_json(r)
assert(contents['name'] == 'Troll')
assert(contents['link'] == '/race/Troll')
assert(contents['faction'] == 'horde')
assert(contents['playableClass'] == 'Druid, Hunter, Mage, Priest, Rogue, Shaman, Warlock, Warrior, Death Knight, Monk')

# Testing a GET on /race/Human/description
print("   Testing '/race/<raceName>/description' path...")
r = client.get(base_url + '/race/Dog/description')
assert(r.status_code == 404)
r = client.get(base_url + '/race/Human/description')
assert(r.status_code == 200)
contents = get_json(r)
assert('description' in contents)
assert(contents['description'] == "Recent discoveries have shown that humans are descended from the barbaric vrykul, half-giant warriors who live in Northrend. Early humans were primarily a scattered and tribal people for several millennia, until the rising strength of the troll empire forced their strategic unification. Thus the nation of Arathor was formed, along with its capital, the city-state of Strom.")

# Testing a GET on /race/Highmountain Tauren/description
r = client.get(base_url + '/race/Highmountain%20Tauren/description')
assert(r.status_code == 200)
contents = get_json(r)
assert('description' in contents)
assert(contents['description'] == "Descended from Huln, brave hero of the War of the Ancients, the Highmountain tauren honor the spirits of earth, river, and sky. Though the Legion invaded their lands and sowed seeds of distrust between them, the tribes of Highmountain stand united once more. At long last they are ready to venture beyond their sacred mountain and stand beside their kin from Kalimdor, lending their nobility and strength to the mighty Horde.")

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
r = client.get(base_url + '/class/Warrior' + 'www')
assert(r.status_code == 404)
r = client.get(base_url + '/class/Warrior')
assert(r.status_code == 200)
contents = get_json(r)
assert(contents['class name'] == 'Warrior')
assert(contents['link'] == '/class/Warrior')
assert(contents['power type'] == 'rage')
assert(contents['roles'] == 'DPS, Tank')

# Testing a GET on /class/Druid
r = client.get(base_url + '/class/LeeroyJenkins')
assert(r.status_code == 404)
r = client.get(base_url + '/class/Druid')
assert(r.status_code == 200)
contents = get_json(r)
assert(contents['class name'] == 'Druid')
assert(contents['link'] == '/class/Druid')
assert(contents['power type'] == 'mana')
assert(contents['roles'] == 'DPS, Tank, Healer')

# Testing a GET on /faction
print("   Testing '/faction' path...")
r = client.get(base_url + '/faction/')
assert(r.status_code == 200)
r = client.get(base_url + '/faction')
assert(r.status_code == 200)
contents = get_json(r)
assert('factions' in contents)
assert(contents['factions'][0]['name'] == 'Alliance')
assert(contents['factions'][1]['name'] == 'Horde')

# Testing a GET on /faction/Alliance
print("   Testing '/faction/<factionName>' path...")
r = client.get(base_url + '/faction/Alliance' + 'LeeroyJenkins')
assert(r.status_code == 404)
r = client.get(base_url + '/faction/Alliance')
assert(r.status_code == 200)
contents = get_json(r)
assert('name' in contents)
assert(contents['name'] == "Alliance")
assert('description' in contents)
assert(contents['description'] is not None)

# Testing a GET on /faction/Horde
r = client.get(base_url + '/faction/Horde' + 'LeeroyJenkins')
assert(r.status_code == 404)
r = client.get(base_url + '/faction/Horde')
assert(r.status_code == 200)
contents = get_json(r)
assert('name' in contents)
assert(contents['name'] == "Horde")
assert('description' in contents)
assert(contents['description'] is not None)

# Testing a GET on /role
print("   Testing '/role' path...")
r = client.get(base_url + '/role/')
assert(r.status_code == 200)
r = client.get(base_url + '/role')
assert(r.status_code == 200)
contents = get_json(r)
assert('roles' in contents)
assert(contents['roles'][0]['name'] == 'Tank')
assert(contents['roles'][1]['name'] == 'Healer')
assert(contents['roles'][2]['name'] == 'Damage Dealer (DPS)')

# Testing a GET on /role/Damage Dealer (DPS)
print("   Testing '/role/<roleName>' path...")
r = client.get(base_url + '/role/Damage Dealer (DPS)' + 'LeeroyJenkins')
assert(r.status_code == 404)
r = client.get(base_url + '/role/Damage Dealer (DPS)')
assert(r.status_code == 200)
contents = get_json(r)
assert('name' in contents)
assert(contents['name'] == "Damage Dealer (DPS)")
assert('description' in contents)
assert(contents['description'] is not None)
assert(contents['description'] == "Damage dealers focus on the critical task of dealing damage to the party's foes.")

# Testing a GET on /battlegroup
print("   Testing '/battlegroup' path...")
r = client.get('/battlegroup' + 'fail')
assert(r.status_code == 404)
r = client.get('/battlegroup')
assert(r.status_code == 200)
contents = get_json(r)
assert("battlegroups" in contents)
assert(len(contents["battlegroups"]) == 9)

# Testing a GET on /2v2arena
print("   Testing '/2v2arena' path...")
r = client.get('/2v2arena' + 'hello')
assert(r.status_code == 404)
r = client.get('/2v2arena')
assert(r.status_code == 200)
contents = get_json(r)
assert("2v2arena" in contents)
assert(contents['2v2arena']['info'] == "The /2v2arena endpoints in this API provide different statistics and information based on the top 5000 players in the WoW 2v2 ladder.")

# Testing a GET on /2v2arena/highestRankedPlayer
print("   Testing '/2v2arena/highestRankedPlayer' path...")
r = client.get('/2v2arena/highestRankedPlayer' + 'hello')
assert(r.status_code == 404)
r = client.get('/2v2arena/highestRankedPlayer')
assert(r.status_code == 200)
contents = get_json(r)
assert("player" in contents)
assert(len(contents) == 1)
assert('name' in contents['player'])
assert('rating' in contents['player'])

# Testing a GET on /2v2arena/gladiatorTotal
print("   Testing '/2v2arena/gladiatorTotal' path...")
r = client.get('/2v2arena/gladiatorTotal' + 'hello')
assert(r.status_code == 404)
r = client.get('/2v2arena/gladiatorTotal')
assert(r.status_code == 200)
contents = get_json(r)
assert("gladiators" in contents)

# Testing a GET on /2v2arena/topServers
print("   Testing '/2v2arena/topServers' path...")
r = client.get('/2v2arena/topServers' + 'hello')
assert(r.status_code == 404)
r = client.get('/2v2arena/topServers')
assert(r.status_code == 200)
contents = get_json(r)
assert("servers" in contents)

# Testing a GET on /3v3arena
print("   Testing '/3v3arena' path...")
r = client.get('/3v3arena' + 'hello')
assert(r.status_code == 404)
r = client.get('/3v3arena')
assert(r.status_code == 200)
contents = get_json(r)
assert("3v3arena" in contents)
assert(contents['3v3arena']['info'] == "The /3v3arena endpoints in this API provide different statistics and information based on the top 5000 players in the WoW 3v3 ladder.")

# Testing a GET on /3v3arena/highestRankedPlayer
print("   Testing '/3v3arena/highestRankedPlayer' path...")
r = client.get('/3v3arena/highestRankedPlayer' + 'hello')
assert(r.status_code == 404)
r = client.get('/3v3arena/highestRankedPlayer')
assert(r.status_code == 200)
contents = get_json(r)
assert("player" in contents)
assert(len(contents) == 1)
assert('name' in contents['player'])
assert('rating' in contents['player'])

# Testing a GET on /3v3arena/gladiatorTotal
print("   Testing '/3v3arena/gladiatorTotal' path...")
r = client.get('/3v3arena/gladiatorTotal' + 'hello')
assert(r.status_code == 404)
r = client.get('/3v3arena/gladiatorTotal')
assert(r.status_code == 200)
contents = get_json(r)
assert("gladiators" in contents)

# Testing a GET on /3v3arena/topServers
print("   Testing '/3v3arena/topServers' path...")
r = client.get('/3v3arena/topServers' + 'hello')
assert(r.status_code == 404)
r = client.get('/3v3arena/topServers')
assert(r.status_code == 200)
contents = get_json(r)
assert("servers" in contents)

# Testing a GET on /RBG
print("   Testing '/RBG' path...")
r = client.get('/RBG' + 'hello')
assert(r.status_code == 404)
r = client.get('/RBG')
assert(r.status_code == 200)
contents = get_json(r)
assert("RBG" in contents)
assert(contents['RBG']['info'] == "The /RBG endpoints in this API provide different statistics and information based on the top 5000 players in the WoW RBG ladder.")

# Testing a GET on /RBG/highestRankedPlayer
print("   Testing '/RBG/highestRankedPlayer' path...")
r = client.get('/RBG/highestRankedPlayer' + 'hello')
assert(r.status_code == 404)
r = client.get('/RBG/highestRankedPlayer')
assert(r.status_code == 200)
contents = get_json(r)
assert("player" in contents)
assert(len(contents) == 1)
assert('name' in contents['player'])
assert('rating' in contents['player'])

# Testing a GET on /RBG/gladiatorTotal
print("   Testing '/RBG/gladiatorTotal' path...")
r = client.get('/RBG/gladiatorTotal' + 'hello')
assert(r.status_code == 404)
r = client.get('/RBG/gladiatorTotal')
assert(r.status_code == 200)
contents = get_json(r)
assert("gladiators" in contents)

# Testing a GET on /RBG/topServers
print("   Testing '/RBG/topServers' path...")
r = client.get('/RBG/topServers' + 'hello')
assert(r.status_code == 404)
r = client.get('/RBG/topServers')
assert(r.status_code == 200)
contents = get_json(r)
assert("servers" in contents)

print("############### API TESTS DONE ##################")