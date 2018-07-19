#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa starting with N"""
import sys
import MySQLdb


def main(argv):

    if len(argv) - 1 != 3:
        print("Must enter 4 arguments")
        return

    db = MySQLdb.connect (host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                          db=argv[3],
                          port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC")

    for row in cur.fetchall():
        print (row)

    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
