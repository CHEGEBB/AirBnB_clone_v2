#!/usr/bin/python3

import MySQLdb

connection = MySQLdb.connect(host="localhost",
                             user="hbnb_test",
                             passwd="hbnb_test_pwd",
                             db="hbnb_test_db",
                             charset="utf8")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM states")
initial_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM states")
final_count = cursor.fetchone()[0]

assert final_count - initial_count == 1, "Creating a new state did not add a record to the database"

cursor.close()
connection.close()
