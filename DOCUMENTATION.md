# Documentation on API endpoints

/race                         -- this path returns the list of playable races
```
    {'races': [
        {
            'link': '/race/Human', 
            'name': 'Human'
        }, ...
    ]} 
```


/race/"raceName"              -- this route returns information on the given race
```
    {
        'faction': 'alliance', 
        'link': '/race/Human', 
        'name': 'Human',
        'playableClasses': 'Hunter, Mage, Paladin, Priest, Rogue, Warlock, Warrior, Death Knight, Monk'
    }
```


/race/"raceName"/description  -- this route returns a description of the given race
```
    {
        'description': 'Recent discoveries have shown that humans are descended from the barbaric vrykul, half-giant warriors who live in                      Northrend. Early humans were primarily a scattered and tribal people for several millennia, until the rising strength                  of the troll empire forced their strategic unification. Thus the nation of Arathor was formed, along with its capital,                 the city-state of Strom.'
    }
```


/class                        -- this route returns a list of playable classes
```
    {'classes': [
        {
            'class name': 'Warrior',
            'link': '/class/Warrior'
        }, ...
    ]}
```


/class/"className"            -- this route returns information on a given class
```
    {
        'class name': 'Warrior', 
        'link': '/class/Warrior', 
        'power type': 'rage', 
        'roles': 'DPS, Tank'
    }
```


/faction                      -- this route returns both faction names
```
    {'factions': [
        {
            'link': '/faction/Alliance', 
            'name': 'Alliance'
        }, 
        {
            'link': '/faction/Horde', 
            'name': 'Horde'
        }
    ]}
```

/faction/"factionName"        -- this returns a brief summary on a specific faction
```
    {
        'description': 'The Alliance, also known as the Grand Alliance, is one of two major political factions of the mortal races in Azeroth, its counterpart being the Horde. The Alliance consists of powerful cultures and groups bound not by desperation or necessity, but by their deep commitments to abstract concepts like nobility and justice, and, striving to represent these high ideals, its many different peoples all contribute their technical, arcane, and spiritual wisdom "toward the goal of a just and peaceful world."', 
        'link': '/faction/Alliance', 
        'name': 'Alliance'
    }
```

/role                         -- this route returns list of playable roles in the game
```
    {'roles': [
        {
            'link': '/role/Tank', 
            'name': 'Tank'
        }, 
        {
            'link': '/role/Healer', 
            'name': 'Healer'
        }, 
        {
            'link': '/role/Damage%20Dealer%20%28DPS%29', 
            'name': 'Damage Dealer (DPS)'
        }
    ]}
```

/role/"roleName"              -- this route returns info on a specific role
```
    {
        'description': "Damage dealers focus on the critical task of dealing damage to the party's foes.", 
        'link': '/role/Damage%20Dealer%20%28DPS%29',
        'name': 'Damage Dealer (DPS)'
    }
```

/battlegroups                 -- this route returns list of all the battlegroups
```
    {'battlegroups': [
        {'battlegroup name': 'AU/NZ Battle Group'}, 
        {'battlegroup name': 'Bloodlust'}, 
        {'battlegroup name': 'Cyclone'}, 
        {'battlegroup name': 'Rampage'}, 
        {'battlegroup name': 'Reckoning'}, 
        {'battlegroup name': 'Ruin'}, 
        {'battlegroup name': 'Shadowburn'}, 
        {'battlegroup name': 'Vengeance'}, 
        {'battlegroup name': 'Vindication'}
    ]}
```

/2v2arena                     -- this route returns some info on the 2v2 pvp leaderboard
```
    {
        'info': 'The /2v2arena endpoints in this API provide different statistics and information based on the top 5000 players in the WoW 2v2 ladder.'
    }
```

/2v2arena/highestRankedPlayer -- this route returns the top player in the 2v2 ladder and their rating
```
    {
        'name': 'Floormat', 
        'rating': '2932'
    }
```

/2v2arena/gladiatorTotal      -- this route returns the total number of gladiators in the 2v2 ladder
```
    {'number': '1120'}
```

/2v2arena/topServers          -- this route returns the top five servers with most players in the top 5000 on the 2v2 ladder
```
    {
        'servers': '[(\'Tichondrius\', 812), 
                     (\'Illidan\', 341), 
                     ("Kel\'Thuzad", 273), 
                     (\'Sargeras\', 269),
                     ("Mal\'Ganis", 224)]'
    }
```

/3v3arena                     -- this route returns some info on the 3v3 pvp leaderboard
```
    {
        'info': 'The /3v3arena endpoints in this API provide different statistics and information based on the top 5000 players in the WoW 3v3 ladder.'
    }
```

/3v3arena/highestRankedPlayer -- this route returns the top player in the 3v3 ladder and their rating
```
    {
        'name': 'Floormat', 
        'rating': '2932'
    }
```

/3v3arena/gladiatorTotal      -- this route returns the total number of gladiators in the 3v3 ladder
```
    {'number': '1120'}
```

/3v3arena/topServers          -- this route returns the top five servers with most players in the top 5000 on the 3v3 ladder
```
    {
        'servers': '[(\'Tichondrius\', 812), 
                     (\'Illidan\', 341), 
                     ("Kel\'Thuzad", 273), 
                     (\'Sargeras\', 269),
                     ("Mal\'Ganis", 224)]'
    }
```

/RBG                          -- this route returns some info on the RBG pvp leaderboard
```
    {
        'info': 'The /RBG endpoints in this API provide different statistics and information based on the top 5000 players in the WoW RBG ladder.'
    }
```

/RBG/highestRankedPlayer      -- this route returns the top player in the RBG ladder and their rating
```
    {
        'name': 'Floormat', 
        'rating': '2932'
    }
```

/RBG/gladiatorTotal           -- this route returns the total number of gladiators in the RBG ladder
```
    {'number': '1120'}
```

/RBG/topServers               -- this route returns the top five servers with most players in the top 5000 on the RBG ladder
```
    {
        'servers': '[(\'Tichondrius\', 812), 
                     (\'Illidan\', 341), 
                     ("Kel\'Thuzad", 273), 
                     (\'Sargeras\', 269),
                     ("Mal\'Ganis", 224)]'
    }
```
