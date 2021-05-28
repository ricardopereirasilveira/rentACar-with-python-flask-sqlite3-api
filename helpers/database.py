import sqlite3

class databaseFunctions:
    def __init__(self):
        self.__connection = sqlite3.connect('database.db', check_same_thread=False)
        self.__cursor = self.__connection.cursor()

    def createDatabase(self, name: str) -> None:
        """
        Method used to create a database if not created, using the SQLITE3 library.
        :param name: It will receive the name of database to create it after access
                     some pages, if database exists, it will no create anymore.
        :return: It return None, because its only necessary to create the database.
        """
        createTable = f"""
        CREATE TABLE IF NOT EXISTS {name} (
        id INTEGER,
        'First Name' VARCHAR(50) NOT NULL,
        'Last Name' VARCHAR(50) NOT NULL,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50) NOT NULL,
        PRIMARY KEY (id, username)
        )
        """
        self.execute(createTable)

    def insertUser(self, id_account: int, firstname: str, lastname: str, username: str, password: str) -> None:
        """
        This method insert the user from /create-user to insert into database
        :param id_account: The ID ( unique ) of the user, it will get the last ID and will increment one more to add to
                            database.
        :param firstname: The first name of user, received from form.
        :param lastname: The last name of user, received from form.
        :param username: The username, it was choice by user and will check if has it on database. If the username
                            was in use, it return a error and tell to user insert a new username.
        :param password: The passoword sent from username, it encrypt and send the password to databse.
        :return: it return None, because after insert, it will redirect to login page
        """
        insertUser = f"INSERT INTO user (id, 'First Name', 'Last Name', username, password) " \
                     f"VALUES ({id_account}, '{firstname}', '{lastname}', '{username}', '{password}')"
        self.execute(insertUser)

    def verifyUsernameExists(self, username: str) -> True or False:
        """
        That method will check if X username exists in database and will return a validation
        to verify.
        :sql query: SELECT EXISTS(SELECT 1 FROM myTbl WHERE u_tag="tag");
        :param username: Receive the param to verify if account exists in database
        :return: TRUE if user not exists in database and FALSE if user exists in database
        """
        query = f"SELECT * FROM user WHERE username = '{username}'"
        self.__cursor.execute(query)
        return self.__cursor.fetchone() is None

    # TODO: Try/Execpt to catch a error if it occours.
    def execute(self, script) -> None:
        """
        That method is used to run the query in database, its only necessary
        to send the query and it will execute and close the database.
        :param script: Send the complet query and it will execute in database.
        :return: It return None, because after complet the execution, it will
                close the datase.
        """
        try:
            self.__cursor.execute(script)
            self.__connection.commit()
            self.__connection.close()
        except Exception as e:
            print(e)

    # TODO: Caso não exista usuário, ajustar para ter o ID 1
    def verifyLastAdded(self):
        query = f"SELECT * FROM user ORDER BY id DESC LIMIT 1"
        self.__cursor.execute(query)
        user = int(self.__cursor.fetchone()[0])
        user += 1
        return user

    def verifyUsernameAndPwd(self, username: str) -> list:
        # SELECT * FROM user WHERE username = ''
        query = f"SELECT * FROM user WHERE username = '{username}'"
        self.__cursor.execute(query)
        return self.__cursor.fetchone()
