#!/usr/bin/python3

"""
lists all cities by state from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user, passwd, db_name = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    sql = """SELECT cities.id, cities.name, states.name FROM cities
          JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC"""
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
