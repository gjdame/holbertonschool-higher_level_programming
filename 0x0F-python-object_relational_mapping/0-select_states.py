#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb


def main(argv):

    if len(argv) - 1 != 3:
        print("Must enter 3 arguments")
        return

    db = MySQLdb.connect (host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                          db=argv[3],
                          port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print (row)

    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
