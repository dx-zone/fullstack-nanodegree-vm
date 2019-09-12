#!/usr/bin/env python

# Populating the database with anothe python script
# import sqlalchemy functions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import base restaurant and menu classes
from database_setup import Base, Restaurant, MenuItem

# engine function to for the database engine communication
engine = create_engine('sqlite:///restaurantmenu.db')

# bind the engine to the Base class
# to make connections between our class definitions and
# the corresponding tables  within the database
Base.metadata.bind = engine

# establish link of communication between our code
# executions and the engine created
DBSession = sessionmaker(bind = engine)

# sqlalchemy execute SQL commands via an interface named sessions
# this will hold all the SQL command to be sent but don't commit them
session = DBSession()

# -- Create, Read, Update, Delete (CRUD)

# Lines of example code for CRUD
#newEntry = ClassName(property = "value",...)
#session.add(newEntry)
#session.commit()

# Make an entry to "Restaurant" table, into "name" column
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

# query "Restaurant" table to find entire entries
session.query(Restaurant).all()

# Make multiple entries to "MenuItem" table and
# specify the ForeignKey relationship "myFirstRestaurant"
cheesepizza = MenuItem(name = "Cheese Pizza", \
	description = "Made with all natural ingredients and fresh mozzarella", \
	course = "Entry", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()

# query "MenuItem" table to find entire entries
session.query(MenuItem).all()

