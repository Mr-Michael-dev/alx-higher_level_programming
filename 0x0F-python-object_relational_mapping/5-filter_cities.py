#!/usr/bin/python3

"""
Takes in 4 arguments and displays all cities from the cities table
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


def filter_cities_by_state(cursor, db, state_name):
    """Filters cities.name based on the provided state name."""

    # Escape for SQL injection prevention
    sanitized_name = db.escape_string(state_name)
    query = """SELECT cities.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC"""
    cursor.execute(query, (sanitized_name,))
    return cursor.fetchall()


def main():
    """Main function to handle program execution."""
    cursor = None
    db = None
    username, password, database, state_name = sys.argv[1:]

    if len(sys.argv) != 5:
        print("""Usage: ./2-my_filter_states.py < mysql username >
              < mysql password > < database name > < state name searched >""")
        exit(1)

    try:
        db = connect_to_database(username, password, database)
        cursor = db.cursor()
        cities = filter_cities_by_state(cursor, db, state_name)

        print(", ".join(city[0] for city in cities))

    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()
