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

# Particular page requested. The specific query string will be
# appended to that.
page = 'data/character/classes?locale=en_US&access_token=USma7h4s9q8efPJyQpwfTlj5t5ogbi0NaD'

# This just combines our base_url and page into our request_url
req_url = base_url + page

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

# Puts each class into our database
for eachClass in results['classes']:
   db.addClass(eachClass['name'], eachClass['powerType'])
   db.commit()



############## Query for WoW API Battlegroups ################
page = 'data/battlegroups/?locale=en_US&access_token=USZbPYtne1FhueFiwAR7PKRHU8ODXtGwTq'
req_url = base_url + page
response = oauth.get(req_url)
results = json.loads(response.content.decode('utf-8'))
for bg in results['battlegroups']:
	db.addBattlegroup(bg['name'])
	db.commit()


############## Query for Wikipedia WoW Factions ################

# TODO: Setup query for obtaining faction info from wikipedia 
# Use this link for how to do that and read the second answer that talks about the wikipedia Python library
# https://stackoverflow.com/questions/4460921/extract-the-first-paragraph-from-a-wikipedia-article-python







# ## Programming Languages in Wikipedia
# import requests, json, re
# from pprint import pprint
# from bs4 import BeautifulSoup

# # The following function takes as input a full URL.
# # It returns a BeautifulSoup object representing that web page's contents
# # If the page does not exist, it returns None
# def getPage(url):
#    req = requests.get(url)
#    if (req.status_code != 200):
#       return None
#    return BeautifulSoup(req.content, 'html.parser')

# ## You will need to add this to the relative links you may encounter
# baseUrl = "https://wow.gamepedia.com"

# ## This page contains a list of all programming languages that have Wikipedia pages
# listPage = getPage("http://wowwiki.wikia.com/wiki/Alliance")
# listPage.head
# # print(listPage.head)
# print(listPage.find_all('p'))