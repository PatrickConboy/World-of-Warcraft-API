# This file will pull data from various websites and APIs and then put
# that data into our local database.

# Loading libraries needed for authentication and requests
import operator
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from db import Db   # See db.py
import db

db = Db(True)

# In order to use this script, you must:
# - Have a Blizzard API account and create an app in order to obtain a clientID and secret
# - Store in keys.json a property called "blizzardAPI" whose value is an
#     object with two keys, "clientID" and "secret"
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['blizzardAPI']

blizzardAPI_clientID = keys['clientID']
blizzardAPI_secret = keys['secret']

# We authenticate ourselves with the above credentials
#
# For documentation, see http://requests-oauthlib.readthedocs.io/en/latest/api.html
# and http://docs.python-requests.org/en/master/
client = BackendApplicationClient(client_id=blizzardAPI_clientID)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://US.battle.net/oauth/token',
                          client_id=blizzardAPI_clientID,
                          client_secret=blizzardAPI_secret)

# Base url needed for all subsequent queries
base_url = 'https://us.api.blizzard.com/wow/'

# Setup is done. Now we can access the specific parts of the Blizzard API we want.


############## Query for WoW API Races ################

# Particular page requested. The specific query string will be
# appended to that.
page = 'data/character/races?locale=en_US&access_token=USTncSSBoKRvJ1PGU6la6d6syvxeNyrtqV'

# This just combines our base_url and page into our request_url
req_url = base_url + page

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

# Puts all the information for the individual races into our database
for race in results['races']:
   raceName = race['name']
   if raceName == 'Human':
      db.addRace(race['name'], race['id'], race['side'], "Recent discoveries have shown that humans are descended from the barbaric vrykul, half-giant warriors who live in Northrend. Early humans were primarily a scattered and tribal people for several millennia, until the rising strength of the troll empire forced their strategic unification. Thus the nation of Arathor was formed, along with its capital, the city-state of Strom.")
   elif raceName == 'Dwarf':
      db.addRace(race['name'], race['id'], race['side'], "The bold and courageous dwarves are an ancient race descended from the earthen—beings of living stone created by the titans when the world was young. Due to a strange malady known as the Curse of Flesh, the dwarves’ earthen progenitors underwent a transformation that turned their rocky hides into soft skin. Ultimately, these creatures of flesh and blood dubbed themselves dwarves and carved out the mighty city of Ironforge in the snowy peaks of Khaz Modan.")
   elif raceName == 'Night Elf':
      db.addRace(race['name'], race['id'], race['side'], "The ancient and reclusive night elves have played a pivotal role in shaping Azeroth’s fate. The night elves of today still remember the War of the Ancients over ten thousand years ago, when they halted the Burning Legion’s first invasion of Azeroth. When the Legion’s remnants rallied together with the vile satyrs centuries later, the night elves again opposed the threat, ultimately vanquishing the forces that set out to wreak havoc on their world.")
   elif raceName == 'Gnome':
      db.addRace(race['name'], race['id'], race['side'], "The clever, spunky, and oftentimes eccentric gnomes present a unique paradox among the civilized races of Azeroth. Brilliant inventors with an irrepressibly cheerful disposition, this race has suffered treachery, displacement, and near-genocide. It is their remarkable optimism in the face of such calamity that symbolizes the truly unshakable spirit of the gnomes.​")
   elif raceName == 'Draenei':
      db.addRace(race['name'], race['id'], race['side'], "Long before the fallen titan Sargeras unleashed the Legion on Azeroth, he conquered the world of Argus and its inhabitants, the eredar. Believing that this gifted race would be crucial in his quest to undo all of creation, Sargeras contacted the eredar’s leaders – Kil’jaeden, Archimonde, and Velen, offering them knowledge and power in exchange for their loyalty.")
   elif raceName == 'Worgen':
      db.addRace(race['name'], race['id'], race['side'], "Behind the formidable Greymane Wall, a terrible curse transformed some of the stalwart citizens of the isolated kingdom of Gilneas into nightmarish lupine beasts known as worgen. Human scholars intensely debated the origins of the curse, until it was revealed that the original worgen were not—as previously believed—nightmares from another dimension, but cursed night elf druids.")
   elif raceName == 'Pandaren' and race['side'] == 'neutral':
      db.addRace(race['name'], race['id'], race['side'], "Couched in myth and legend, rarely seen and even more rarely understood, the enigmatic pandaren have long been a mystery to the other races of Azeroth. The noble history of the pandaren people stretches back thousands of years, well before the empires of man and before even the sundering of the world.")
   elif raceName == 'Pandaren' and race['side'] == 'horde' or raceName == 'Pandaren' and race['side'] == 'alliance':
      pass
   elif raceName == 'Orc':
      db.addRace(race['name'], race['id'], race['side'], "Unlike the other races of the Horde, orcs are not native to Azeroth. Initially, they lived as shamanic clans on the lush world of Draenor. They abandoned their peaceful culture when Kil’jaeden, a demon lord of the Burning Legion, corrupted the orcs and used them in his vengeful plot against the draenei, who were exiles from Kil’jaeden’s homeworld.")
   elif raceName == 'Undead':
      db.addRace(race['name'], race['id'], race['side'], "Death offered no escape for the scores of humans killed during the Lich King’s campaign to scour the living from Lordaeron. Instead, the kingdom’s fallen were risen into undeath as Scourge minions and forced to wage an unholy war against everything… and everyone… that they once held dear.")
   elif raceName == 'Tauren':
      db.addRace(race['name'], race['id'], race['side'], "The peaceful tauren—known in their own tongue as the shu’halo—have long dwelled in Kalimdor, striving to preserve the balance of nature at the behest of their goddess, the Earth Mother. Until recently, the tauren lived as nomads scattered throughout the Barrens, hunting the great kodo beasts native to the arid region.")
   elif raceName == 'Troll':
      db.addRace(race['name'], race['id'], race['side'], "The savage trolls of Azeroth are infamous for their cruelty, dark mysticism, and seething hatred for all other races. Yet one exception among the trolls is the Darkspear tribe. Plagued by a history of subservience and exile, this proud tribe was on the brink of extinction when Warchief Thrall and his mighty Horde forces were driven to the trolls’ remote island home in the South Seas during a violent storm.")
   elif raceName == 'Blood Elf':
      db.addRace(race['name'], race['id'], race['side'], "For nearly 7,000 years, high elven society centered on the sacred Sunwell, a magical fount that was created using a vial of pure arcane energy from the first Well of Eternity. Nourished and strengthened by the Sunwell’s potent energies, the high elves’ enchanted kingdom of Quel’Thalas prospered within the verdant forests north of Lordaeron.")
   elif raceName == 'Goblin':
      db.addRace(race['name'], race['id'], race['side'], "Originally the slaves of jungle trolls on the Isle of Kezan, goblins were forced to mine kaja’mite ore out of the volcanic bowels of Mount Kajaro. The trolls used this potent mineral for their voodoo rituals, but it had an unexpected effect on the slaves who were in constant contact with it: kaja’mite generated new cunning and intelligence in the goblin race.")
   elif raceName == 'Dark Iron Dwarf':
      db.addRace(race['name'], race['id'], race['side'], "Known for their fiery tempers and fierce determination, Dark Iron dwarves have a turbulent history with the other clans. A failed coup in Ironforge ignited the War of the Three Hammers, and many of the Dark Iron once fought in the service of Ragnaros the Firelord. Though one faction of the dwarves is pledged to Queen-Regent Moira Thaurissan, others refuse to stand alongside their kin. The Alliance seeks a united Dark Iron clan to harness the power of Azerite and aid their struggle against the Horde.")
   elif raceName == 'Lightforged Draenei':
      db.addRace(race['name'], race['id'], race['side'], "For untold millennia, the Army of the Light waged war against the Burning Legion throughout the Twisting Nether. The draenei most committed to their long crusade would undergo a ritual to become Lightforged, infusing their bodies with the very essence of the Holy Light. After finally achieving victory on Argus, the Lightforged draenei have undertaken a new mission: protecting Azeroth from rising threats and helping the Alliance push back against Horde aggression.")
   elif raceName == 'Void Elf':
      db.addRace(race['name'], race['id'], race['side'], "Many have sought to harness the corruptive magic of the Void. Most who tried have fallen into madness. Determined to use this power for the good of Azeroth, Alleria Windrunner is the first mortal to succeed at defying the shadow's whispers. Coming to the aid of a group of her kin who nearly gave in to the darkness, Alleria has vowed to train these Void Elves to control the shadows within them and pledge their newfound powers to the Alliance.")
   elif raceName == 'Highmountain Tauren':
      db.addRace(race['name'], race['id'], race['side'], "Descended from Huln, brave hero of the War of the Ancients, the Highmountain tauren honor the spirits of earth, river, and sky. Though the Legion invaded their lands and sowed seeds of distrust between them, the tribes of Highmountain stand united once more. At long last they are ready to venture beyond their sacred mountain and stand beside their kin from Kalimdor, lending their nobility and strength to the mighty Horde.")
   elif raceName == "Mag'har Orc":
      db.addRace(race['name'], race['id'], race['side'], "For untold generations, the orc clans of Draenor battled one another in endless war. But when Gul'dan offered them the blood of his demonic masters, the disparate tribes of Mag'har—the orcish word for 'uncorrupted'—refused the dark bargain and banded together to drive out the Burning Legion. In the aftermath of the fall of Hellfire Citadel, the Mag'har pledged to one day repay Azeroth's heroes for aiding their cause. As war against the Alliance intensifies, the Horde must call upon the might of the Mag'har to seize victory.")
   elif raceName == 'Nightborne':
      db.addRace(race['name'], race['id'], race['side'], "Isolated behind a protective barrier for 10,000 years, the elves of Suramar grew increasingly dependent upon the arcane magic of the Nightwell. To protect this font of power, the leaders of the Nightborne struck a bargain with the Burning Legion that plunged their kingdom into civil war. After fighting for freedom from their demonic masters, the Nightborne seek allies in the Horde to help reclaim their place in the world.")
db.commit()

############## Query for WoW API Classes ################

# Explanation of what these individual lines are doing is the
# same as the above query above for WoW API Races
page = 'data/character/classes?locale=en_US&access_token=USma7h4s9q8efPJyQpwfTlj5t5ogbi0NaD'
req_url = base_url + page
response = oauth.get(req_url)
results = json.loads(response.content.decode('utf-8'))

# Puts each class from our query into our database
for eachClass in results['classes']:
   className = eachClass['name']
   if className == 'Warrior' or className == 'Death Knight' or className == 'Demon Hunter':
      db.addClass(eachClass['name'], eachClass['powerType'], "DPS, Tank")
   elif className == 'Druid' or className == 'Monk' or className == 'Paladin':
      db.addClass(eachClass['name'], eachClass['powerType'], "DPS, Tank, Healer")
   elif className == 'Shaman' or className == 'Priest':
      db.addClass(eachClass['name'], eachClass['powerType'], "DPS, Healer")
   elif className == 'Rogue' or className == 'Warlock' or className == 'Mage' or className == 'Hunter':
      db.addClass(eachClass['name'], eachClass['powerType'], "DPS")
db.commit()


############## Adding Faction info into database ################

# Add Alliance info to database
db.addFaction("Alliance", 'The Alliance, also known as the Grand Alliance, is one of two major political factions of the mortal races in Azeroth, its counterpart being the Horde. The Alliance consists of powerful cultures and groups bound not by desperation or necessity, but by their deep commitments to abstract concepts like nobility and justice, and, striving to represent these high ideals, its many different peoples all contribute their technical, arcane, and spiritual wisdom "toward the goal of a just and peaceful world."')

# Add Horde info to database
db.addFaction("Horde", "The Horde (also called the New Horde, Thrall's Horde or Vol'jin's Horde) is one of the two major political factions of the mortal races in Azeroth, its counterpart being the Alliance. The Horde, a faction led by off-worlders and composed of outsiders has survived these obstacles by bonding together, fighting as family, comrades, or even uneasy allies.")
db.commit()


############## Query for WoW API Battlegroups ################

# Explanation of what these individual lines are doing is the
# same as the above query above for WoW API Races
page = 'data/battlegroups/?locale=en_US&access_token=USZbPYtne1FhueFiwAR7PKRHU8ODXtGwTq'
req_url = base_url + page
response = oauth.get(req_url)
results = json.loads(response.content.decode('utf-8'))

# Puts each battlegroup name from our query results into our database
for bg in results['battlegroups']:
	db.addBattlegroup(bg['name'])
db.commit()


############## Query for WoW API 3v3 Arenas ################

# Explanation of what these individual lines are doing is the
# same as the above query above for WoW API Races
page = 'leaderboard/3v3?locale=en_US&access_token=USZbPYtne1FhueFiwAR7PKRHU8ODXtGwTq'
req_url = base_url + page
response = oauth.get(req_url)
results = json.loads(response.content.decode('utf-8'))

# Adds a basic description of the 3v3 ladder
db.addArenaStat("Info", 
               "The /3v3arena endpoints in this API provide different statistics and information based on the top 5000 players in the WoW 3v3 ladder.",
               None)

# Adds highest ranked player to our database for arena stats
db.addArenaStat("Top 3v3 Player", str(results['rows'][0]['rating']), results['rows'][0]['name'])
db.commit()

# This code pulls all players who are in the gladiator tier of the 3v3 arena ladder
# and then counts the number of gladiators and puts that statistic in our database
gladiators  = [player['name'] for player in results['rows'] if player['tier'] == 'Gladiator']
db.addArenaStat("Number of 3v3 Gladiators", str(len(gladiators)), None)
db.commit()

# Put all server name mentions into a dictionary and count how many times each server mentioned
serverCounts = {}
for player in results['rows']:
   if player['realmName'] in serverCounts:
      serverCounts[player['realmName']] += 1
   else:
      serverCounts[player['realmName']] = 1

# Sort our dictionary of server names by the number of times each server was mentioned
sortedServerCounts = sorted(serverCounts.items(), key=operator.itemgetter(1), reverse=True)

# Take out the first 5 servers mentioned in our dictionary and put them into a list
topFive = []
for i in range(0,5):
  topFive.append(sortedServerCounts[i])

# Add our top 5 server list to the database
db.addArenaStat("Top 3v3 Servers", str(topFive), None)
db.commit()