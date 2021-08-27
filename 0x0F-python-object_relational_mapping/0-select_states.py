#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    host = "localhost"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    port = 3306

    # Open database connection
    db = MySQLdb.connect(host, user, passwd, db, port)

    sql = "SELECT * FROM states ORDER BY states.id ASC"
    db.execute(sql)
    data = db.fetchall()
    for row in data:
        print(row)
    db.close()
