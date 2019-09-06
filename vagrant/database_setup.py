#!/usr/bin/env python

import os
import sys

try:
    from sqlalchemy import Column, ForeignKey, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship
    from sqlalchemy import create_engine

except Exception as e:
    print(e)
    print("Install the sqlalchemy module by \
executing: 'pip install sqlalchemy'")

Base = declarative_base()


class Restaurant(Base):
    """ """
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)


class MenuItem(Base):
    """ """
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
