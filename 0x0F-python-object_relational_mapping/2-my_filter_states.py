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

    c.execute("SELECT * FROM states ORDER BY(id) ASC")
    result = c.fetchall()
    [print(x) for x in result if x[1] == argv[4].strip()]

    c.close()
    db.close()
