#!/usr/bin/python3
"""lists all states from database hbtn_0e_0_usa starting with N"""
import sys
import MySQLdb


def main(argv):

    if len(argv) - 1 != 4:
        print("Must enter 4 arguments")
        return

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name\
        FROM cities INNER JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s ORDER BY cities.id ASC", [
            argv[4]])

    res = []
    for row in cur.fetchall():
        res.append(row)

    for i in range(len(res)):
        res[i] = str(res[i])
        res[i] = res[i].strip(')')
        res[i] = res[i].strip('(')
        res[i] = res[i].strip("'")
        res[i] = res[i].strip(",")
        res[i] = res[i].strip("'")
    res = ', '.join(res)
    print(res)

    db.close()


if __name__ == "__main__":
    import sys
    main(sys.argv)
