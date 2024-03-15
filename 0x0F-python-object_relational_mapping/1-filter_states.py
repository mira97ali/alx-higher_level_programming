#!/usr/bin/python3
"""Filter States"""
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
    cursor.execute(
        """ SELECT * FROM states WHERE name
            LIKE BINARY 'N%' ORDER BY states.id """
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
