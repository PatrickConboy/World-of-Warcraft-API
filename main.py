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

# This route allows user to get the list of all the races in our database
@app.route('/race', methods = ['GET'])
def race_list():
   races = db.getRaces()
   return make_json_response({
      "races": [
         {
            "name": race.name,
            "link": url_for('race_info', raceName=race.name)
         }
         for race in races
      ]
   })

# This route allows user to get a specific race from the database when they
# pass in a race name
@app.route('/race/<raceName>', methods = ['GET'])
def race_info(raceName):
   race = db.getRace(raceName)
   if race is None:
       abort(404, 'unknown race name')
   return make_json_response({
      "name": race.name,
      "faction": race.faction,
      "playableClass": race.playableClass,
      "link": url_for('race_info', raceName=race.name)
   })

# This route ives back the description of the specific race
@app.route('/race/<raceName>/description', methods = ['GET'])
def race_description(raceName):
   race = db.getRace(raceName)
   if race is None:
       abort(404, 'unknown race name')
   return make_json_response({
      "description": race.description
   })

# This route gives back the list of classes
@app.route('/class', methods = ['GET'])
def class_list():
   classes = db.getClasses()
   if classes == None:
      abort(404, 'classes not found')
   return make_json_response({
      "classes": [
         {
            "class name": eachClass.name,
            "link": url_for('class_info', className=eachClass.name)
         }
         for eachClass in classes
      ]
   })

# This route gives back information of specific class(power type, role)
@app.route('/class/<className>', methods = ['GET'])
def class_info(className):
   givenClass = db.getClass(className)
   if givenClass is None:
       abort(404, 'unknown class name')
   return make_json_response({
      "class name": givenClass.name,
      "power type": givenClass.powerType,
      "roles": givenClass.roles,
      "link": url_for('class_info', className=givenClass.name)
   })

# This route gives back the list of factions
@app.route('/faction', methods = ['GET'])
def faction_list():
   factions = db.getFactions()
   if factions == None:
      abort(404, 'factions not found')
   return make_json_response({
      "factions": [
         {
            "name": faction.name,
            "link": url_for('faction_info', factionName=faction.name)
         }
         for faction in factions
      ]
   })

# This route gives back description of specific faction
@app.route('/faction/<factionName>', methods = ['GET'])
def faction_info(factionName):
   faction = db.getFaction(factionName)
   if faction is None:
       abort(404, 'unknown faction name')
   return make_json_response({
      "name": faction.name,
      "description": faction.description,
      "link": url_for('faction_info', factionName=faction.name)
   })


# This route gives back the list of roles
@app.route('/role', methods = ['GET'])
def role_list():
   roles = db.getRoles()
   return make_json_response({
      "roles": [
         {
            "name": role.name,
            "link": url_for('role_info', roleName=role.name)
         }
         for role in roles
      ]
   })


# This route gives back description of specific role
@app.route('/role/<roleName>', methods = ['GET'])
def role_info(roleName):
   role = db.getRole(roleName)
   if role is None:
       abort(404, 'unknown role name')
   return make_json_response({
      "name": role.name,
      "description": role.description,
      "link": url_for('role_info', roleName=role.name)
   })


# This route gives back the list of battlegroups
@app.route('/battlegroup', methods = ['GET'])
def battlegroup_list():
   battlegroups = db.getBattlegroups()
   if battlegroups == None:
      abort(404, 'battlegroups not found not found')
   return make_json_response({
      "battlegroups": [
         {
            "battlegroup name": bg.name
         }
         for bg in battlegroups
      ]
   })

# This route returns basic info on the 2v2 ladder
@app.route('/2v2arena', methods = ['GET'])
def info_for_2v2_ladder():
   arenaInfo = db.getArenaStat("2v2 Info")
   if arenaInfo == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "2v2arena":
         {
            "info": arenaInfo.statistic
         }
   })

# This route returns the name and rating of the highest ranked player in the 2v2 ladder
@app.route('/2v2arena/highestRankedPlayer', methods = ['GET'])
def highest_rank_2v2():
   highestRank = db.getArenaStat("Top 2v2 Player")
   if highestRank == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "player":
         {
            "name": highestRank.description,
            "rating": highestRank.statistic
         }
   })

# This route returns the total number of gladiators currently in the 2v2 ladder
@app.route('/2v2arena/gladiatorTotal', methods = ['GET'])
def number_of_2v2_gladiators():
   gladiators = db.getArenaStat("Number of 2v2 Gladiators")
   if gladiators == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "gladiators":
         {
            "number": gladiators.statistic
         }
   })

# This route returns the top 5 servers with the most gladiators on them in the 2v2 ladder
@app.route('/2v2arena/topServers', methods = ['GET'])
def top_2v2_servers():
   servers = db.getArenaStat("Top 2v2 Servers")
   if servers == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "servers":
         {
            "name": servers.statistic
         }
   })

# This route returns basic info on the 3v3 ladder
@app.route('/3v3arena', methods = ['GET'])
def info_for_3v3_ladder():
   arenaInfo = db.getArenaStat("3v3 Info")
   if arenaInfo == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "3v3arena":
         {
            "info": arenaInfo.statistic
         }
   })

# This route returns the name and rating of the highest ranked player in the 3v3 ladder
@app.route('/3v3arena/highestRankedPlayer', methods = ['GET'])
def highest_rank_3v3():
   highestRank = db.getArenaStat("Top 3v3 Player")
   if highestRank == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "player":
         {
            "name": highestRank.description,
            "rating": highestRank.statistic
         }
   })

# This route returns the total number of gladiators currently in the 3v3 ladder
@app.route('/3v3arena/gladiatorTotal', methods = ['GET'])
def number_of_3v3_gladiators():
   gladiators = db.getArenaStat("Number of 3v3 Gladiators")
   if gladiators == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "gladiators":
         {
            "number": gladiators.statistic
         }
   })

# This route returns the top 5 servers with the most gladiators on them in the 3v3 ladder
@app.route('/3v3arena/topServers', methods = ['GET'])
def top_3v3_servers():
   servers = db.getArenaStat("Top 3v3 Servers")
   if servers == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "servers":
         {
            "name": servers.statistic
         }
   })

# This route returns basic info on the rbg ladder
@app.route('/RBG', methods = ['GET'])
def info_for_rbg_ladder():
   arenaInfo = db.getArenaStat("rbg Info")
   if arenaInfo == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "RBG":
         {
            "info": arenaInfo.statistic
         }
   })

# This route returns the name and rating of the highest ranked player in the rbg ladder
@app.route('/RBG/highestRankedPlayer', methods = ['GET'])
def highest_rank_rbg():
   highestRank = db.getArenaStat("Top rbg Player")
   if highestRank == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "player":
         {
            "name": highestRank.description,
            "rating": highestRank.statistic
         }
   })

# This route returns the total number of gladiators currently in the rbg ladder
@app.route('/RBG/gladiatorTotal', methods = ['GET'])
def number_of_rbg_gladiators():
   gladiators = db.getArenaStat("Number of rbg Gladiators")
   if gladiators == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "gladiators":
         {
            "number": gladiators.statistic
         }
   })

# This route returns the top 5 servers with the most gladiators on them in the rbg ladder
@app.route('/RBG/topServers', methods = ['GET'])
def top_rbg_servers():
   servers = db.getArenaStat("Top rbg Servers")
   if servers == None:
      abort(404, 'statistic not found')
   return make_json_response({
      "servers":
         {
            "name": servers.statistic
         }
   })

## HELPER METHODS

## Helper method for creating JSON responses
def make_json_response(content, response = 200, headers = {}):
   headers['Content-Type'] = 'application/json'
   return make_response(json.dumps(content), response, headers)

# Starts the application
if __name__ == "__main__":
   app.run()