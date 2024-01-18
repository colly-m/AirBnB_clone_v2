#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel):
    """ The city class, contains state ID and name
    Attrib:
        state_id: The state id
        name: imputed name
    """
    __tablename = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
