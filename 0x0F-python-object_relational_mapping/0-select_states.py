#!/usr/bin/python3
""" Usage: {:s} <username> <password> <database> """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv, exit

    if len(argv) != 4:
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
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for row in states:
        print(row)
