import sqlite3

connection = sqlite3.connect('db.db', check_same_thread=False)
cursor = connection.cursor()

createTable = """CREATE TABLE IF NOT EXISTS test (
id INTEGER UNIQUE,
'First Name' VARCHAR(50) NOT NULL,
'Last Name' VARCHAR(50) NOT NULL,
username VARCHAR(50) UNIQUE,
  PRIMARY KEY (id, username)
)

"""


cursor.execute(createTable)
connection.commit()
connection.close()