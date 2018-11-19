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

@app.route('/race', methods = ['GET'])
def race_list():
   races = db.getRaces()
   return make_json_response({
      "races": [
         {
            "name": race.name,
            "faction": race.faction,
            "description": race.description
         }
         for race in races
      ]
   })

@app.route('/race/<race>', methods = ['GET'])
def race_info(raceName):
   race = db.getRace(raceName)
   return make_json_response({
      "name": race.name,
      "faction": race.faction,
      "description": race.description
   })



## HELPER METHODS

## Helper method for creating JSON responses
def make_json_response(content, response = 200, headers = {}):
   headers['Content-Type'] = 'application/json'
   return make_response(json.dumps(content), response, headers)


# Starts the application
if __name__ == "__main__":
   app.run()