from flask import Flask
from flask_restful import Api, Resource

from models.user import databaseFunctions, allUsersApiModel, usersApiModel


# Creating a Flask Aplication
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py')
app.secret_key = 'testing'


# Creating a API service
api = Api(app)
api.add_resource(allUsersApiModel, '/api/user/all')
api.add_resource(usersApiModel, '/api/user/<string:username>')


# Importing all views
from views.all_views import *


if __name__ == '__main__':
    app.run(debug=True)