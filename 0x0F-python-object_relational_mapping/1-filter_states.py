#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database
    )

    c = db.cursor()

    c.execute("SELECT * FROM states WHERE LEFT(name, 1) = 'N' ORDER BY(id) ASC")
    [print(x) for x in c.fetchall()]

    c.close()
    db.close()