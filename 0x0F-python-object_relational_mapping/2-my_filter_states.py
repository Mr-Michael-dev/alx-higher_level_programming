#!/usr/bin/python3

"""
The Script contains a function that accesses a databas
accepts argumnets and run operations base on arguments passed

Usage: ./2-my_filter_states.py <mysql username>
       <mysql password> <database name> <state name searched>
"""
import MySQLdb
import sys


def main():
    """
    Displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    sql = """SELECT * FROM states WHERE name LIKE BINARY '{}'
          ORDER BY id ASC""".format(sys.argv[4])

    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
