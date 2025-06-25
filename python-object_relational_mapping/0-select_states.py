#!/usr/bin/env python3

"""
Script that lists all states from the database hbtn_0e_0_usa,
sorted by id ascending.
Takes 3 arguments: mysql username, mysql password, and database name.
"""


import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)

cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
