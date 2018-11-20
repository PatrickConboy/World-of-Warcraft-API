# This script will access the World of Warcraft API

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
   db.addRace(race['name'], race['id'], race['side'], "test")
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


############## Query for Wikipedia WoW Factions ################

# TODO: Setup query for obtaining faction info from wikipedia 
# Use this link for how to do that and read the second answer that talks about the wikipedia Python library
# https://stackoverflow.com/questions/4460921/extract-the-first-paragraph-from-a-wikipedia-article-python