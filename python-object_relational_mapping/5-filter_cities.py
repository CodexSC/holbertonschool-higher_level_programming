#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    state_name = sys.argv[4]
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    cities = [row[0] for row in cur.fetchall()]
    if cities:
        print(", ".join(cities))
    else:
        print("")
    cur.close()
    db.close()
