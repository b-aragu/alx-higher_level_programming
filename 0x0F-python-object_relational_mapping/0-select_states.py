#!/usr/bin/python3
'''Write a script that lists all states from the database hbtn_0e_0_usa:'''
import MySQLdb
import sys


def list_states(username, password, database):
    '''function to list the states'''
    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)
