# Project for CS328 - Data Management/Data Wrangling
# Coded by: Od Ganzorig and Patrick Conboy
# Date Created: 9/18/2018
# Project Description: Our project pulls data from various websites and API's,
# puts that data into our database, and then implements a basic web API that a user
# can use to access the World of Warcraft info stored in our database.

# GO HERE FOR API DOCUMENTATION: https://develop.battle.net/documentation/api-reference/world-of-warcraft-community-api

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

# TODO: Setup @app.route for /class and /className
@app.route('/class', methods = ['GET'])
def class_list():
   classes = db.getClasses()
   return make_json_response({
      "classes": [
         {
            "class name": eachClass.name,
            "power type": eachClass.powerType,
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
      "link": url_for('class_info', className=givenClass.name)
   })

# TODO: Setup @app.route for /faction and /faction/factionName

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