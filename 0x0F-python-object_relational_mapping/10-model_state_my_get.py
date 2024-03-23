#!/usr/bin/python3
'''Prints the first State object from a given database'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def listStateArg(username, password, database, arg):
    '''prints first state of a database'''
    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    states = session.query(State).filter(State.name.like(arg)).all()

    # print output
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    # close session
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) < 5):
        print('Usage: ./8-model_state_fetch_first.py')
        sys.exit(1)

    # assignement
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]

    # call function
    listStateArg(username, password, database, arg)
