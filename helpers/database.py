import sqlite3


class databaseFunctions:
    connection = sqlite3.connect('database.db', check_same_thread=False)
    cursor = connection.cursor()
    def __init__(self):
        pass

    def createDatabase(self, name):
        createTable = """CREATE TABLE IF NOT EXISTS user (
            id SERIAL,
            'First Name' VARCHAR(50),
            'Last Name' VARCHAR(50),
            'Username' VARCHAR(50),
            'Password' VARCHAR(50),
            PRIMARY KEY (username)
        )"""
        self.execute(createTable)

    def insertUser(self, firstname, lastname, username, password):
        insertUser = """"""

    def execute(self, script):
        try:
            self.cursor.execute(script)
            self.connection.commit()
            self.connection.close()
        except Exception as e:
            print(e)
