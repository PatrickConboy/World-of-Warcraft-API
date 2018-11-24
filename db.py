# This file will define our database structure and provide methods to
# access our database

# Sets up database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from json import dumps

Base = declarative_base()

# Class for Races. Each race has a unique id, name, and faction
class Race(Base):
   __tablename__ = 'races'

   name        = Column(String(20), nullable = False, primary_key = True)
   id          = Column(Integer, nullable = False, primary_key = True)
   faction     = Column(String(10), nullable = False)
   description = Column(String(500))

   def __repr__(self):
      return "<Race: {0}>".format(self.name)

# Class for Class. Each class has a name, power type, and roles available to that class.
class Class(Base):
   __tablename__ = 'classes'

   name      = Column(String(20), nullable = False, primary_key = True)
   powerType = Column(String(20), nullable = False)
   roles     = Column(String(50))

   def __repr__(self):
      return "<Class Name: {0}>".format(self.name)

# Class for Factions. The two factions have a name and description.
class Faction(Base):
   __tablename__ = 'factions'

   name        = Column(String(20), nullable = False, primary_key = True)
   description = Column(String(400))

   def __repr__(self):
      return "<Faction: {0}>".format(self.name)

# Class for Battlegroup. Each battlegroup has a name.
class Battlegroup(Base):
   __tablename__ = 'battlegroups'

   name = Column(String(20), nullable = False, primary_key = True)

   def __repr__(self):
      return "<Battlegroup Name: {0}>".format(self.name)

class ArenaStat(Base):
   __tablename__ = 'arena_stats'

   name        = Column(String(40), nullable = False, primary_key = True)
   statistic   = Column(String(100), nullable = False)
   description = Column(String(50))

   def __repr__(self):
      return "<Stat Name: {0} -- Stat: {1}>".format(self.name, self.statistic)

# Represents the database and our interaction with it
class Db:
   def __init__(self, refresh = False):
      engineName = 'sqlite:///test.db'   # Uses in-memory database
      self.engine = create_engine(engineName)
      self.metadata = Base.metadata
      self.metadata.bind = self.engine
      if refresh:
         self.metadata.drop_all(bind=self.engine)
         self.metadata.create_all(bind=self.engine)
      Session = sessionmaker(bind=self.engine)
      self.session = Session()

   # Base commit method for our database
   def commit(self):
      self.session.commit()
   # Base rollback method for our database
   def rollback(self):
      self.session.rollback()


   ########## METHODS FOR RACE CLASS ###########

   # Returns the list of all races
   def getRaces(self):
      return self.session.query(Race).all()

   # Returns a specific race when given a race name
   def getRace(self, name):
      return self.session.query(Race)\
                 .filter_by(name=name)\
                 .one_or_none()

   # This method adds a new race to our database when given name, id, faction, and description
   # Returns the Race object that got added
   def addRace(self, name, id, faction, description):
      newRace = Race(name=name, id=id, faction=faction, description=description)
      self.session.add(newRace)
      return newRace


   ########## METHODS FOR CLASS CLASS ###########

   # Returns the list of all classes
   def getClasses(self):
      return self.session.query(Class).all()

   # Returns a specific class when given a class name
   def getClass(self, name):
      return self.session.query(Class)\
                 .filter_by(name=name)\
                 .one_or_none()

   # This method adds a new class to our database when given a className and powerType
   # Returns the Class object that got added
   def addClass(self, name, powerType, roles):
      newClass = Class(name=name, powerType=powerType, roles=roles)
      self.session.add(newClass)
      return newClass


   ########## METHODS FOR FACTION CLASS ###########

   # This method returns the list of factions in WoW
   def getFactions(self):
      return self.session.query(Faction).all()

   # This method returns information on one of the two factions
   # User gives name of which faction they want to learn about
   def getFaction(self, name):
      return self.session.query(Faction)\
                 .filter_by(name=name)\
                 .one_or_none()

   # This method adds a new faction to the database with the given name
   # and description, then returns the new faction that was created
   def addFaction(self, name, description):
      newFaction = Faction(name=name, description=description)
      self.session.add(newFaction)
      return newFaction


   ########## METHODS FOR CLASS BATTLEGROUP ###########

   # This methods returns the list of battlegroups in WoW
   def getBattlegroups(self):
      return self.session.query(Battlegroup).all()

   # This method allows us to add a battlegroup to our database
   def addBattlegroup(self, name):
      newbg = Battlegroup(name=name)
      self.session.add(newbg)
      return newbg

   # This method returns the list of all arena stats in our database
   def getArenaStats(self):
      return self.session.query(ArenaStat).all()

   # This method returns a specific statistic when given a name of a stat
   def getArenaStat(self, name):
      return self.session.query(ArenaStat)\
                 .filter_by(name=name)\
                 .one_or_none()

   # This method adds a new arena stat to our database
   def addArenaStat(self, name, stat, description):
      newStat = ArenaStat(name=name, statistic=stat, description=description,)
      self.session.add(newStat)
      return newStat