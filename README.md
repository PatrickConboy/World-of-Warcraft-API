# Project for CS328 - Data Management/Data Wrangling
# Coded by: Od Ganzorig and Patrick Conboy
# Date Created: 9/18/2018
# Project Description: Our project pulls data from various websites and API's,
# puts that data into our database, and then implements a basic web API that a user
# can use to access the World of Warcraft info stored in our database.


                    API Paths

/                             -- TODO: this path will return a list of possible API paths (low priority)

/race                         -- this path returns the list of playable races
/race/<raceName>              -- this path returns information on a specific race
/race/<raceName>/description  -- this path returns a description of the race
/race/<raceName>/class        -- this path returns playable classes for a given race (low priority)

/class                        -- this path returns a list of playable classes
/class/<className>            -- this path returns information on a given class.

/faction                      -- this path returns both faction names
/faction/<factionName>        -- this returns a brief summary on a specific faction

/role                         -- this path returns list of playable roles in the game (high priority)
/role/<roleName>              -- this path returns info on a specific role (Name, description) (high priority)

/2v2arena                     -- returns some info on the 2v2 pvp leaderboard (low priority)
/2v2arena/highestRankedPlayer -- returns the top player in the 2v2 ladder and their rating (low priority)
/2v2arena/gladiatorTotal      -- returns the total number of gladiators in the 2v2 ladder (low priority)
/2v2arena/topServers          -- returns the top five servers with most players in the top 5000 on the 2v2 ladder (low priority)

/3v3arena                     -- returns some info on the 3v3 pvp leaderboard
/3v3arena/highestRankedPlayer -- returns the top player in the 3v3 ladder and their rating
/3v3arena/gladiatorTotal      -- returns the total number of gladiators in the 3v3 ladder
/3v3arena/topServers          -- returns the top five servers with most players in the top 5000 on the 3v3 ladder

/RBG                     -- TODO: returns some info on the RBG pvp leaderboard (low priority)
/RBG/highestRankedPlayer -- TODO: returns the top player in the RBG ladder and their rating (low priority)
/RBG/gladiatorTotal      -- TODO: returns the total number of gladiators in the RBG ladder (low priority)
/RBG/topServers          -- TODO: returns the top five servers with most players in the top 5000 on the RBG ladder (low priority)

/battlegroups                 -- returns list of all the battlegroups

TODO: Some JSON payloads are being returns as a list with a dictionary inside. Might need to change this
      for some of our endpoints (low priority)

      Add db tests for new classes and methods that have been added (high priority)

      Make sure names of methods in main.py are all using underscores and not camel case (high priority)

      Refactor before finishing (high priority)