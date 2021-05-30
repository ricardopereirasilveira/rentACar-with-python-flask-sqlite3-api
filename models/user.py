import sqlite3
from flask_restful import Resource, reqparse
from flask import session


def verifyIfUserIsLogged() -> True or False:
    """
    That param will check if user is logged ( using the session )
    :return: It will return True or False. If user is logged, it will return TRUE, else FALSE
    """
    return 'logged_user' not in session or session['logged_user'] is None


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
    def verifyLastAdded(self) -> int:
        """
        That method verify the last ID from database to increment one more to not reply that
        because the ID is unique
        :return: It a integer with the last id from database + 1
        """
        query = f"SELECT * FROM user ORDER BY id DESC LIMIT 1"
        self.__cursor.execute(query)
        user = int(self.__cursor.fetchone()[0])
        user += 1
        return user

    def verifyUsernameAndPwd(self, username: str) -> list:
        """
        That method is to verify if username exists in database
        :param username: receive the username from front-end to verify the account
        :return: it return a list with all parameters if user is find, to check the password.
        """
        # SELECT * FROM user WHERE username = ''
        query = f"SELECT * FROM user WHERE username = '{username}'"
        self.__cursor.execute(query)
        return self.__cursor.fetchone()

    def returningAllUsersFromDatabase(self):
        query = "SELECT * FROM user"
        self.__cursor.execute(query)
        return self.__cursor.fetchall()


class allUsersApiModel(Resource):
    def get(self) -> []:
        users = []
        for x in databaseFunctions().returningAllUsersFromDatabase():
            users.append(
                {
                    'id': x[0],
                    'First Name': x[1],
                    'Last Name': x[2],
                    'Username': x[3]
                }
            )
        return users, 200


class usersApiModel(Resource):
    args = reqparse.RequestParser()

    def __init__(self, id_user=None, firstname=None, lastname=None, username=None):
        self.__id_user = id_user
        self.__firstname = firstname
        self.__lastname = lastname
        self.__username = username

    def json(self):
        return {
            'id': self.__id_user,
            'First Name': self.__firstname,
            'Last Name': self.__lastname,
            'Username': self.__username
        }

    def get(self, username: str) -> dict:
        user = databaseFunctions().verifyUsernameAndPwd(username)
        if user is None:
            return {'message': 'user not found!'}
        self.__id_user = user[0]
        self.__firstname = user[1]
        self.__lastname = user[2]
        self.__username = user[3]
        return self.json()

    def put(self, username: str) -> dict:
        pass

    def delete(self, username: str) -> dict:
        pass
