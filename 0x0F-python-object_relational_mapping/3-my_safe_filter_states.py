#!/usr/bin/python3

"""
Takes in 4 arguments and displays all values from the states table
of hbtn_0e_0_usa where name matches the state name searched.

Arguments:
    1. mysql username
    2. mysql password
    3. database name
    4. state name searched

Usage: ./2-my_filter_states.py <mysql username> <mysql password>
       <database name> <state name searched>
"""

import MySQLdb
import sys


def connect_to_database(username, password, database):
    """Connects to the MySQL database."""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        return db
    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")
        exit(1)


def filter_states(cursor, state_name):
    """Filters states based on the provided state name."""

    # Escape for SQL injection prevention
    sanitized_name = "%{}%".format(cursor.escape_string(state_name))
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sanitized_name,))
    return cursor.fetchall()


def main():
    """Main function to handle program execution."""
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py < mysql username >
              < mysql password > < database name > < state name searched >")
        exit(1)

        username, password, database, state_name = sys.argv[1:]

    try:
        db = connect_to_database(username, password, database)
        cursor = db.cursor()
        results = filter_states(cursor, state_name)

        for row in results:
            print(row)

    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
