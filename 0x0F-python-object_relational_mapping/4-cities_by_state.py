#!/usr/bin/python3
""" Usage: {:s} <username> <password> <database> """


if __name__ == "__main__":
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
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM states INNER JOIN cities\
                   states.id = cities.state_id ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for row in cities:
        print(row)
    cursor.close()
    database.close()
