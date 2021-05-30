from flask import render_template, session

from app import app
from models.user import databaseFunctions, verifyIfUserIsLogged
from helper.greeting import returningGreeting


@app.route('/')
def index():
    if verifyIfUserIsLogged():
        informations = {'logged_user': False}
    else:
        informations = {'logged_user': True,
                        'user_name': databaseFunctions().verifyUsernameAndPwd(session['logged_user'])[1],
                        'user_id': databaseFunctions().verifyUsernameAndPwd(session['logged_user'])[0]
                        }
    informations.update({'greeting': returningGreeting()})
    return render_template('index.html', info=informations)
