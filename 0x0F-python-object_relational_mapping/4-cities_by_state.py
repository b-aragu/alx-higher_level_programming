#!/usr/bin/python3
'''Lists all all cities from a given database'''

import sys
import MySQLdb


def listCities(username, password, database):
    '''function to list cities of a given database'''
    # connect to server
    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database)
    # create cursor object
    cursor = db.cursor()

    # SQL statement
    cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities INNER JOIN states "
            "ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch and print cities
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # close cursor and database
    cursor.close()
    db.close()


if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print("Usage: ./4-cities_by_states username password database")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # call function
    listCities(username, password, database)
