# Sets up database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from json import dumps

# Loading libraries needed for authentication and requests
import operator
import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

Base = declarative_base()

# Class for Races. Each race has a unique id, name, and faction
class Race(Base):
   __tablename__ = 'races'

   name        = Column(String(20), nullable = False, primary_key = True)
   id          = Column(Integer, nullable = False)
   faction     = Column(String(10), nullable = False)
   description = Column(String(200))

   def __repr__(self):
      return "Race <{0} Faction: {1}>".format(self.name, self.faction)

# Represents the database and our interaction with it
class Db:
   def __init__(self):
      engineName = 'sqlite:///test.db'   # Uses in-memory database
      self.engine = create_engine(engineName)
      self.metadata = Base.metadata
      self.metadata.bind = self.engine
      self.metadata.drop_all(bind=self.engine)
      self.metadata.create_all(bind=self.engine)
      Session = sessionmaker(bind=self.engine)
      self.session = Session()

   def commit(self):
      self.session.commit()

   def rollback(self):
      self.session.rollback()

   # Returns the list of all races
   def getRaces(self):
      return self.session.query(Race).all()

   # Returns a specific race when given a race name
   def getRace(self, name):
      return self.session.query(Race)\
                 .filter_by(name=name)\
                 .one_or_none()

############## Begin Building Database #############


############## Begin Web Requests ##################

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

for race in results['races']:
  print(race['name'])
