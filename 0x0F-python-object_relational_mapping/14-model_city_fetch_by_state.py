#!/usr/bin/python3
'''Prints all City objects from  given database'''

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


def listCity(username, password, database):
    '''List city objects'''
    # connct to database
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # sql query
    cities = session.query(State, City).join(
            City, State.id == City.state_id).order_by(City.id).all()

    # print results
    for city, state in cities:
        print('{}: ({}) {}'.format(city.name, city.id, state.name))

    session.close()


if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print('Fewer arguments')
        sys.exit(1)

    # assignment
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function
    listCity(username, password, database)
