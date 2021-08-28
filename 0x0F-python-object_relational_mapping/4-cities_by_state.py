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
    cursor.execute("SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    data = cursor.fetchone()
    while (data):
        print(data)
        data = cursor.fetchone()
