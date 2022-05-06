#!/usr/bin/python3
""" Usage: {:s} <username> <password> <database> """


if __name__ == "__main__":
    import sys
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 5:
        print("Usage: {:s} <username> <password> <database>".format(argv[0]))
        exit(99)

    usrname = argv[1]
    passwd = argv[2]
    dbname = argv[3]

    database = MySQLdb.Connect(
        user=usrname,
        passwd=passwd,
        db=dbname,
        port=3306)
    cursor = database.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY '{:s}'
            ORDER BY states.id ASC""".format(sys.argv[4])
    cursor.execute(query)
    states = cursor.fetchall()
    for row in states:
        print(row)
