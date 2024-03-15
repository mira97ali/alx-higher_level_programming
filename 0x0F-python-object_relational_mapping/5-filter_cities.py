#!/usr/bin/python3
"""Filter Cities"""
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
    curor = database.cursor()
    curor.execute(
        """ SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s """,
        (sys.argv[4],)
    )
    print(*[row[0] for row in curor.fetchall()], sep=", ")
    curor.close()
    database.close()
