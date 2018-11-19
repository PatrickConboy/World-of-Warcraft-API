# Project for CS328 - Data Management/Data Wrangling
# Coded by: Od Ganzorig and Patrick Conboy
# Date Created: 9/18/2018
# Project Description: Web API that provides our user with information on World of Warcraft,
# the factions, races, classes, abilities, and some statistics.

# GO HERE FOR API DOCUMENTATION: https://develop.battle.net/documentation/api-reference/world-of-warcraft-community-api

#!/usr/bin/python3

# Accessing the Blizzard: World of Warcraft API
# This script will access the World of Warcraft API

# Loading libraries needed for authentication and requests
import operator
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

# In order to use this script, you must:
# - Have a Blizzard API account and create an app in order to obtain a clientID and secret
# - Store in keys.json a property called "blizzardAPI" whose value is an
#     object with two keys, "clientID" and "secret"
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['blizzardAPI']

blizzardAPI_clientID = keys['clientID']
blizzardAPI_secret = keys['secret']

# We authenticate ourselves with the above credentials
# We will demystify this process later
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

# Particular page requested. The specific query string will be
# appended to that.
page = 'data/character/races?locale=en_US&access_token=USTncSSBoKRvJ1PGU6la6d6syvxeNyrtqV'

                # END OF AUTHENTICATION AND OAUTH STUFF #


             # BEGINNING OF INDIVIDUAL QUERIES FOR EACH HERO #


# This just combines our base_url and page into our request_url
req_url = base_url + page

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)
# print(response.content)

# Read the query results
results = json.loads(response.content.decode('utf-8'))
# print(results['races'][0])

# for race in results['races']:
#   print(race['name'])

