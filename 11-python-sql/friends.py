import sqlite3

# connect to DB. It will create one if DB doesnt exist
connection = sqlite3.connect('my_friends.db')

# create a cursor object
c = connection.cursor()

# execute some sql commands
#c.execute('CREATE TABLE friends (first_name TEXT, last_name TEXT, age  INTEGER);')

# to insert - use this method to avoid SQL injection!
# data = ('Steve', 'Smith', 55)
# query = 'INSERT INTO friends VALUES (?,?,?)'
# c.execute(query, data)

# bulk insert
# people = [
#     ('Rollo', 'Kent', 15),
#     ('May', 'Chow', 30)
#     ]
# c.executemany('INSERT INTO friends VALUES (?,?,?)', people)

# commit changes
connection.commit()

# never forget to close the connection once done
connection.close()
