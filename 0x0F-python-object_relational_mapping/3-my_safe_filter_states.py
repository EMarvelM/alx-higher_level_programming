#!/usr/bin/python3

"""

"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # extrating the arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]
        values = argv[4]

        db = MySQLdb.connect(
            user = username,
            passwd = password,
            db = database,
        )

        c = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY(id) ASC;"
        c.execute(query, (values,))
        [print(i) for i in c.fetchall()]

    except MySQLdb.Error as e:
        print('Error: ' + e)

    finally:
        if c:
            c.close()
        if db:
            db.close()

