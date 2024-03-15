#!/usr/bin/python3
"""My Safe Filter States"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = database.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()