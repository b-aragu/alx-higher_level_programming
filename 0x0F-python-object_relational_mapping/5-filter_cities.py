#!/usr/bin/python3
'''Lists all all cities from a given database'''

import sys
import MySQLdb


def listCitiesArg(username, password, database, arg):
    '''function to list cities of a given database'''
    # connect to server
    db = MySQLdb.connect(
            host='localhost', port=3306, user=username,
            passwd=password, db=database)
    # create cursor object
    cursor = db.cursor()

    # SQL statement
    queryTemp = ("SELECT cities.name FROM cities INNER JOIN states "
            "ON cities.state_id = states.id WHERE states.name LIKE % s "
            "ORDER BY cities.id ASC")
    cursor.execute(queryTemp, (arg, ))

    # Fetch and print cities
    cities = cursor.fetchall()
    for index, item in enumerate(cities):
        city = item[0]
        if index < len(cities) - 1:
            print(city, end=', ')
        else:
            print(city)

    # close cursor and database
    cursor.close()
    db.close()


if __name__ == '__main__':
    if (len(sys.argv) < 5):
        print("Usage: ./4-cities_by_states username password database")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    arg = sys.argv[4]

    # call function
    listCitiesArg(username, password, database, arg)
