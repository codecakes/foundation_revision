#!/usr/bin/env python

"""
List all restaurants: /list - Read
Each list item has Edit, Delete option

New - Create a new restaurnt with a form- /new

Edit - Update Restaurant with form - /restaurnt/id/edit

Delete Restaurnt - /restaurnt/id/delete, confirmation page that sends POST cmd to ORM for delete
"""

import os
import sys
from sqlalchemy.orm import sessionmaker
from db_config import Rest_Base, Emp_Base, Restaurant, Menu, \
Employee, Address, create_engine_db

#create local engines
rest_engine = create_engine_db(Rest_Base, 'restaurantmenu.db')
emp_engine = create_engine_db(Emp_Base, 'employee.db')

#Bind bases to their respective engines - Or Sql cursors
Rest_Base.metadata.bind = rest_engine
Emp_Base.metadata.bind = emp_engine

#create respective sessions
rest_session_DB = sessionmaker(bind=rest_engine)
emp_session_DB = sessionmaker(bind=emp_engine)

#create staging sessions for respective session engines
#No sessions will be finalized unless called with commit
rest_ses = rest_session_DB()
emp_ses = emp_session_DB()

#create
def create_new_rest(rest_name):
    rest_ses.add(Restaurant(name=rest_name))
    rest_ses.commit()

#read/find
def find_rest(rest_name):
    res = rest_ses.query(Restaurant).filter_by(name=rest_name).all()
    if res:
        for name in res:
            if rest_name == name.name: return name
    return None

def find_rest_id(rest_id):
    res = rest_ses.query(Restaurant).filter_by(id_=rest_id).all()
    if res:
        for name in res:
            if rest_id == name.id_: return name
    return None

def find_rest_name_by_id(rest_id):
    res = rest_ses.query(Restaurant).filter_by(id_ = rest_id).one()
    return res if res else None


#update
def edit_rest_name(rest_name, new_name):
    rest = find_rest(rest_name)
    if rest:
        rest.name = new_name
        rest_ses.commit()

def edit_rest_id(rest_id, new_name):
    rest = find_rest_id(rest_id)
    if rest:
        rest.name = new_name
        rest_ses.commit()

#delete
def delete_rest(rest_id):
    rest = find_rest_id(rest_id)
    if rest:
        rest_ses.delete(rest)
        rest_ses.commit()

##list all restaurant
def listrest():
    res = rest_ses.query(Restaurant).all()
    return res