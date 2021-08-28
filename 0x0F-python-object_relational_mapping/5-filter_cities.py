#!/usr/bin/python3
"""
list cities in database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities  \
        WHERE state_id IN \
        (SELECT id FROM states \
        WHERE name LIKE \
        BINARY '{:s}')".format(argv[4]))
    data = cursor.fetchone()
    while (data):
        print(data)
        data = cursor.fetchone()
