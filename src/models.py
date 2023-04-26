import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birthdate = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    eyes = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    capacity = Column(String(250), nullable=False)
    cargo = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surface = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    weather = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="favorites")

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    login = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship("favorites", back_populates="user")

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')