#!/usr/bin/python3
"""My Filter States"""
import sys
import MySQLdb


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
        "SELECT * FROM states WHERE name LIKE BINARY '%s'".format(sys.argv[4])
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
