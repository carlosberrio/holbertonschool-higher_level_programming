#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:
using module MySQLdb (import MySQLdb):
    Connects to a MySQL server running on localhost at port 3306
    Port 3306 is the default port for the MySQL Protocol ( port ), which is used
    by the mysql client, MySQL Connectors, and utilities such as
    mysqldump and mysqlpump."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
                rows = cur.fetchall()
                    for row in rows:
                                print(row)

