#!/usr/bin/python3
"""A database storage engine"""

from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy.exc import InvalidRequestError


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models import base_model
        if cls is None:
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(ob).__name__, ob.id): ob for ob in objs}

    def new(self, obj):
        """Adds obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes of current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes current database session's obj if its not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
