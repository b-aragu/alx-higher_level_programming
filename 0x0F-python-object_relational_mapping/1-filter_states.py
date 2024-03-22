#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_0_usa that
starts with N
"""

import MySQLdb
from sys import argv

"""
Access db to get states
"""

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY STATES.id" ASC)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
