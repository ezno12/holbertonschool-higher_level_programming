#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Open database connection
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)

    sql = "SELECT * FROM states ORDER BY states.id ASC"
    db.execute(sql)
    data = db.fetchall()
    for row in data:
        print(row)
    db.close()
