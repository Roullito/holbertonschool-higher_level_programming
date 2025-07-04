#!/usr/bin/python3
"""Lists all states with a name  matches the argument
from the database hbtn_0e_0_usa."""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    name = sys.argv[4]
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
