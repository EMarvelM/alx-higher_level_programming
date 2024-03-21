#!/usr/bin/python3
"""
    takes in an argument and displays
    all values in the states table of
    hbtn_0e_0_usa where name matches the argument.

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name = %s \
              ORDER BY(id) ASC", (argv[4],))
    result = c.fetchall()
    [print(x) for x in result]

    c.close()
    db.close()
