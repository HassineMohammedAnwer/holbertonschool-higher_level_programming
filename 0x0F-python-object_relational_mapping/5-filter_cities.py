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
    cursor.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id",
                (sys.argv[4], ))
    cities = cursor.fetchall()
    i = 1
    for row in cities:
        if i == len(cities):
            print(row[0])
        else:
            print(row[0], end=", ")
        i = i + 1
