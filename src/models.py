import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



#class Gender(str, enum.Enum):
 #   MALE = "male"
  #  FEMALE = "female"

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(50), nullable=False)
    birthdate = Column(String(250), nullable=False)
    eyes = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    pass

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surface = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    weather = Column(String(250), nullable=False)
    pass

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    capacity = Column(String(250), nullable=False)
    cargo = Column(String(250), nullable=False)
    pass

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    login = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship("favorites", back_populates="user")




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')









