# Project for CS328 - Data Management/Data Wrangling
# Coded by: Od Ganzorig and Patrick Conboy
# Date Created: 9/18/2018
# Project Description: Our project pulls data from various websites and API's,
# puts that data into our database, and then implements a basic web API that a user
# can use to access the World of Warcraft info stored in our database.

                            
                    API Paths

/ -- TODO: this path will return a list of possible API paths (low priority)

/race -- this path returns the list of playable races
/race/<raceName> -- this path returns information on a specific race
/race/<raceName>/description -- this path returns a description of the race
/race/<raceName>/class -- TODO: this path returns playable classes for a given race (low priority)

/class -- done: this path returns a list of playable classes
/class/<className> -- WIP: this path returns information on a given class. ADD INFO ON DPS/HEALER/TANK
/class/<className>/talents -- TODO: this path will return information on the talents for a given class

/faction -- TODO: this path returns both faction names
/faction/<factionName> -- TODO: this returns a brief summary on a specific faction
/faction/<factionName>/race -- TODO: this returns a list of playable races for a given faction

/role -- TODO: this path returns list of playable roles in the game
/role/<roleName> -- TODO: this path returns info on a specific role

TODO: We should try to implement some relationships/foreign_keys for some of this. Need to 
      figure out where we can use those in our database.

Ideas: Pull PVP leaderboard and aggregate some statistics on top ranked pvp players. For instance, list the top 10 servers and the percentage of players from the top 100 players on each server.

Notes: Doesn't seem like we can programmatically match races to the classes available for them. We are probably going to need to hard code in some of this data if we want to include it (we do).