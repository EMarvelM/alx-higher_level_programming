#!/usr/bin/python3

"""lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
                            <mysql password>
                            <database name >
"""

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

    c.execute("SELECT * FROM states WHERE LEFT(name, 1) \
              = 'N' ORDER BY(id) ASC")
    [print(x) for x in c.fetchall()]

    c.close()
    db.close()
