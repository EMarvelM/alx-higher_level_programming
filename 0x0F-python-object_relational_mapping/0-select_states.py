#!/usr/bin/python3
import MySQLdb
from sys import argv

# .0-select_states.py root '' hbtn_0e_0_usa
def connect_db():
    db = MySQLdb.Connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY(ID) ASC")
    result = c.fetchall()

    for i in result:
        if i:
            print(i)


if __name__ == "__main__":
    connect_db()
