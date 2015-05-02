#!/usr/bin/env python

##CONFIG BLOCK##
import os, sys

#import sql orm attribute types and column
from sqlalchemy import Column, ForeignKey, Integer, String

#import base class to create separate base instances
from sqlalchemy.ext.declarative import declarative_base

#Define relationship
from sqlalchemy.orm import relationship

#import engine that creates sql engine for particular sql backend
from sqlalchemy import create_engine


Rest_Base = declarative_base()
Emp_Base = declarative_base()
##CONFIG BLOCK##


#Create Class representation of Tables
class Restaurant(Rest_Base):
    #Table info
    __tablename__ = 'restaurant'

    #mappers
    id_ = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

class Menu(Rest_Base):
    #Table info
    __tablename__ = 'menu_item'

    #mappers
    id_ = Column(Integer, primary_key=True)
    course = Column(String(200), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id_'))
    restaurant = relationship(Restaurant)

class Employee(Emp_Base):
    __tablename__ = 'employee'
    id_ = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Emp_Base):
    __tablename__ = 'address'
    id_ = Column(Integer, primary_key=True)
    street = Column(String(250), nullable=False)
    zip_code = Column(String(10), nullable=False)
    emp_id = Column(Integer, ForeignKey('employee.id_'))
    employee = relationship(Employee)



def create_engine_db(Base, db_name):
    #Create SQL engine config and DB if absent
    engine = create_engine('sqlite:///'+os.path.join('model', db_name))
    Base.metadata.create_all(engine)
    return engine