from flask import Flask
from flask_restful import Api, Resource

from models.user import databaseFunctions, allUsersApiModel, usersApiModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py')
app.secret_key = 'testing'

api = Api(app)

api.add_resource(allUsersApiModel, '/api/user/all')
api.add_resource(usersApiModel, '/api/user/<string:username>')



from views.login_create_user import *
from views.index import *

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)