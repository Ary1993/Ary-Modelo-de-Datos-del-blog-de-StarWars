import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(100), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False, unique=True)
    director = Column(String(50), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    homeworld = relationship(Planets)
    films_id= Column(Integer, ForeignKey("films.id"))
    films = relationship(Films)




class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(Users)
    planet_id = Column(Integer, ForeignKey("planets.id"))
    planet = relationship(Planets)
   


class Character_Films(Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    character = relationship(Characters)
    films_id = Column(Integer, ForeignKey("Films.id"))
    films = relationship(Films)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
