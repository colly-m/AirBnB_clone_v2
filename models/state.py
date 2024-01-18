#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import shlex
from os import getenv


class State(BaseModel, Base):
    """ State class with Attrib: name: input name"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                                backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            r_cities = []
            cities = storage.all(City)
            for city in cities.value():
                if city.state_id == self.id:
                    r_cities.append(city)
                return r_cities
