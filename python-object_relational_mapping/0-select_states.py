#!/usr/bin/env python3

"""
Script that lists all states from the database hbtn_0e_0_usa, sorted by id ascending.
Uses MySQLdb and dotenv for credentials.
"""

import MySQLdb
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PWD")
database = os.environ.get("MYSQL_DB")

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
