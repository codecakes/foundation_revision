#!/usr/bin/env python
import os
import sys
from sqlalchemy.orm import sessionmaker
from model.db_config import Rest_Base, Emp_Base, Restaurant, Menu, \
Employee, Address, create_engine_db

if __name__ == "__main__":
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