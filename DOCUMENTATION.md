/race                         -- this path returns the list of playable races
```
    {'races': [
        {
            'link': '/race/Human', 
            'name': 'Human'
        }, ...
    ]} 
```

/race/"raceName"              -- this path returns information on the given race
```
    {
        'faction': 'alliance', 
        'link': '/race/Human', 
        'name': 'Human',
        'playableClasses': 'Hunter, Mage, Paladin, Priest, Rogue, Warlock, Warrior, Death Knight, Monk'
    }
```
  
/race/"raceName"/description  -- this path returns a description of the given race
```
    {
        'description': 'Recent discoveries have shown that humans are descended from the barbaric vrykul, half-giant warriors who live in Northrend. Early humans were primarily a scattered and tribal people for several millennia, until the rising strength of the troll empire forced their strategic unification. Thus the nation of Arathor was formed, along with its capital, the city-state of Strom.'
    }
```

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
