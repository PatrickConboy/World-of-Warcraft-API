# World of Warcraft API
This API serves as the final project for CS 328.

# Game data
The API is read-only and provides the user access to various bits of game information, highlighted below.

# API Basic Info
WoW API was developed and runs fine on Linux terminals. Has not been tested on a Windows terminal, but does run on Windows if using a Linux terminal such as Cmder.

WoW API has a few requirements if you want to clone and use the code:
- Python 3 or greater
- Preferably a Linux-based terminal to run on
- SQL Alchemy, Flask, requests_oauthlib, and oauthlib.oauth2 must all be installed

**Note:** This API is hosted on heroku and requests can be made using the following base url: https://worldofwarcraft-api.herokuapp.com/

# API Documentation

Base Url for API: https://worldofwarcraft-api.herokuapp.com/

/race                         -- this path returns the list of playable races
    {'races': [
        {
            'link': '/race/Human', 
            'name': 'Human'
        }, ...
    ]} 

/race/"raceName"              -- this path returns information on a specific race
  
/race/"raceName"/description  -- this path returns a description of the race

/class                        -- this path returns a list of playable classes

/class/"className"            -- this path returns information on a given class

/faction                      -- this path returns both faction names

/faction/"factionName"        -- this returns a brief summary on a specific faction

/role                         -- this path returns list of playable roles in the game

/role/"roleName"              -- this path returns info on a specific role

/battlegroups                 -- returns list of all the battlegroups

/2v2arena                     -- returns some info on the 2v2 pvp leaderboard

/2v2arena/highestRankedPlayer -- returns the top player in the 2v2 ladder and their rating

/2v2arena/gladiatorTotal      -- returns the total number of gladiators in the 2v2 ladder

/2v2arena/topServers          -- returns the top five servers with most players in the top 5000 on the 2v2 ladder

/3v3arena                     -- returns some info on the 3v3 pvp leaderboard

/3v3arena/highestRankedPlayer -- returns the top player in the 3v3 ladder and their rating

/3v3arena/gladiatorTotal      -- returns the total number of gladiators in the 3v3 ladder

/3v3arena/topServers          -- returns the top five servers with most players in the top 5000 on the 3v3 ladder

/RBG                          -- returns some info on the RBG pvp leaderboard

/RBG/highestRankedPlayer      -- returns the top player in the RBG ladder and their rating

/RBG/gladiatorTotal           -- returns the total number of gladiators in the RBG ladder

/RBG/topServers               -- returns the top five servers with most players in the top 5000 on the RBG ladder
