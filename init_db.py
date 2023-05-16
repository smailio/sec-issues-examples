import sqlite3

# Create a connection to the SQLite database
connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# Create the 'movies' table
cursor.execute('''CREATE TABLE movies
                  (title TEXT, year INTEGER)''')

# Create the 'users' table
cursor.execute('''CREATE TABLE users
                  (password_hash TEXT)''')

# Insert example data into the 'movies' table
movies_data = [
    ('Movie 1', 2020),
    ('Movie 2', 2019),
    ('Movie 3', 2021)
]
cursor.executemany('INSERT INTO movies VALUES (?, ?)', movies_data)

# Insert example data into the 'users' table
users_data = [
    ('d8578edf8458ce06fbc5bb76a58c5ca4',),  # Example password hash
    ('5f4dcc3b5aa765d61d8327deb882cf99',),  # Another example password hash
    ('098f6bcd4621d373cade4e832627b4f6',)   # Yet another example password hash
]
cursor.executemany('INSERT INTO users VALUES (?)', users_data)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("SQLite database 'movies.db' created and populated with example data.")
