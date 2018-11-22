# This file defines the paths in our API

from flask import Flask, request, make_response, json, url_for, abort
import web_requests
from db import Db   # See db.py

app = Flask(__name__)
db = Db()
app.debug = True # Comment out when not testing
app.url_map.strict_slashes = False   # Allows for a trailing slash on routes
#### ERROR HANDLERS

@app.errorhandler(500)
def server_error(e):
   return make_json_response({ 'error': 'unexpected server error' }, 500)

@app.errorhandler(404)
def not_found(e):
   return make_json_response({ 'error': e.description }, 404)

@app.errorhandler(403)
def forbidden(e):
   return make_json_response({ 'error': e.description }, 403)

@app.errorhandler(400)
def client_error(e):
   return make_json_response({ 'error': e.description }, 400)


#### MAIN ROUTES

# This route '/race' allows user to get the list of all the races in our database
@app.route('/race', methods = ['GET'])
def race_list():
   races = db.getRaces()
   return make_json_response({
      "races": [
         {
            "name": race.name,
            "faction": race.faction,
            "description": race.description,
            "link": url_for('race_info', raceName=race.name)
         }
         for race in races
      ]
   })

# This route '/race/<raceName>' allows user to get a specific race from the database when they
# pass in a race name
@app.route('/race/<raceName>', methods = ['GET'])
def race_info(raceName):
   if raceName is None:
      abort(404, 'must provide race name')
   race = db.getRace(raceName)
   if race is None:
       abort(404, 'unknown race name')
   return make_json_response({
      "name": race.name,
      "faction": race.faction,
      "description": race.description,
      "link": url_for('race_info', raceName=race.name)
   })


@app.route('/class', methods = ['GET'])
def class_list():
   classes = db.getClasses()
   return make_json_response({
      "classes": [
         {
            "class name": eachClass.name,
            "link": url_for('class_info', className=eachClass.name)
         }
         for eachClass in classes
      ]
   })

@app.route('/class/<className>', methods = ['GET'])
def class_info(className):
   if className is None:
      abort(404, 'must provide class name')
   givenClass = db.getClass(className)
   if givenClass is None:
       abort(404, 'unknown class name')
   return make_json_response({
      "class name": givenClass.name,
      "power type": givenClass.powerType,
      "roles": givenClass.roles,
      "link": url_for('class_info', className=givenClass.name)
   })


# TODO: Setup @app.route for /battlegroup
@app.route('/battlegroup', methods = ['GET'])
def battlegroup_list():
   battlegroups = db.getBattlegroups()
   return make_json_response({
      "battlegroups": [
         {
            "battlegroup name": bg.name
         }
         for bg in battlegroups
      ]
   })



# TODO: Setup @app.route for /faction and /faction/factionName

#@app.route('/faction', methods = ['GET'])
#def faction_list():
   #factions = db.getFactions()
   #return make_json_response({
      #"factions": [
         #{
            #"name": faction.name,
            #"description": factions.description,
            #"link": url_for('faction_info', factionName=faction.name)
         #}
         #for faction in factions
      #]
   #})

#@app.route('/faction/<factionName>', methods = ['GET'])
#def faction_info(factionName):
   #if factionName is None:
      #abort(404, 'must provide faction name')
   #faction = db.getFaction(factionName)
   #if faction is None:
       #abort(404, 'unknown faction name')
   #return make_json_response({
      #"name": faction.name,
      #"description": faction.description,
      #"link": url_for('faction_info', factionName=faction.name)
   #})



# TODO: Possibly implement extra routes for something like /race/raceName/class 
# This would let you see what classes are playable for that specific race
# Might need to implement a few extra routes like this


## HELPER METHODS

## Helper method for creating JSON responses
def make_json_response(content, response = 200, headers = {}):
   headers['Content-Type'] = 'application/json'
   return make_response(json.dumps(content), response, headers)


# Starts the application
if __name__ == "__main__":
   app.run()