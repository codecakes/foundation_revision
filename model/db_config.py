#!/usr/bin/env python

##CONFIG BLOCK##
import os, sys
import sqlite3

#import sql orm attribute types and column
from sqlalchemy import Column, ForeignKey, Integer, String, \
DateTime, func

#import base class to create separate base instances
from sqlalchemy.ext.declarative import declarative_base

#Define relationship
#esp helpful: http://stackoverflow.com/questions/5033547/sqlachemy-cascade-delete
#and http://stackoverflow.com/questions/5033547/sqlachemy-cascade-delete
from sqlalchemy.orm import relationship, backref

#import engine that creates sql engine for particular sql backend
from sqlalchemy import create_engine


Rest_Base = declarative_base()
#Menu_Base = declarative_base()
#Emp_Base = declarative_base()
##CONFIG BLOCK##


#Create Class representation of Tables
class Restaurant(Rest_Base):
    #Table info
    __tablename__ = 'restaurant'

    #mappers
    id_ = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    #A Restaurant can have many menus
    menus = relationship("Menu", \
                        backref="restaurant", cascade='delete,delete-orphan,all')
    #A Restaurant can have many employees
    employees = relationship("Employee", \
                        backref="restaurant", cascade='delete,delete-orphan,all')

class Menu(Rest_Base):
    #Table info
    __tablename__ = 'menu'

    #mappers
    id_ = Column(Integer, primary_key=True)
    menuname = Column(String(200), nullable=False)
    course = Column(String(200), nullable=False)
    description = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id_'))
    #restaurant = relationship(Restaurant)

class Employee(Rest_Base):
    __tablename__ = 'employee'
    id_ = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id_'))
    #An Employee has One to One relationship with Employee's Address
    emp_address = relationship("EmpAddress", \
                                backref='employee', uselist=False,\
                                cascade='delete,delete-orphan,all')

class EmpAddress(Rest_Base):
    __tablename__ = 'address'
    id_ = Column(Integer, primary_key=True)
    street = Column(String(250), nullable=False)
    zip_code = Column(String(10), nullable=False)
    emp_id = Column(Integer, ForeignKey('employee.id_'))
    #employee = relationship(Employee)



def create_engine_db(Base, db_name):
    #Create SQL engine config and DB if absent
    engine = create_engine('sqlite:///'+os.path.join('model', db_name), echo=True)
    Base.metadata.create_all(engine)
    return engine