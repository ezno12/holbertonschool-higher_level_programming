#!/usr/bin/python3
"""
connect to database
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
    name = argv[4]
    # Drop table if it already exist using execute() method.
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
    ORDER BY id ASC",  (name, ))
    data = cursor.fetchall()
    for i in data:
        print(i)

    cursor.close()
    db.close()
