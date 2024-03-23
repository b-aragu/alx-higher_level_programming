#!/usr/bin/python3
'''Lists allState objects from the given databse'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def listState(username, password, database):
    '''Fuction to list all state objects'''
    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, database), pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query states and sort by id
    states = session.query(State).order_by(State.id).all()

    # print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close session
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print("Usage: ./7-model username password database")
        sys.exit(1)

    # assignment
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function
    listState(username, password, database)
