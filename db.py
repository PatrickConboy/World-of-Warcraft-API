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
   description = Column(String(200))

   def __repr__(self):
      return "<Race: {0} -- Faction: {1}>".format(self.name, self.faction)

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

   def commit(self):
      self.session.commit()

   def rollback(self):
      self.session.rollback()

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
