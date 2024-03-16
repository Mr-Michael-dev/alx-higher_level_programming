#!/usr/bin/python3

"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument

Usage: ./2-my_filter_states.py <mysql username>
       <mysql password> <database name> <state name searched>
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE
                %s ORDER BY id ASC", (sys.argv[4] + '%'))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
