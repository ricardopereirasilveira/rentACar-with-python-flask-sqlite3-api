from flask import render_template, redirect, url_for, request, flash
import bcrypt

from helpers.database import databaseFunctions
from app import app


@app.route('/create-user')
def create_user():
    try:
        databaseFunctions().createDatabase('user')
    except Exception as e:
        print(e)
    return render_template('create_user.html')


# TODO: Criar o teste para verificar se funciona perfeitamente
@app.route('/creatinguser', methods=['POST', ])
def creating_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if not databaseFunctions().verifyUsernameExists(username):
        flash('This account is currently in use on the website. Please, use another to register.')
        return redirect(url_for('create_user'))

    if password == confirm_password:
        password_encrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt(7))
        id_account = databaseFunctions().verifyLastAdded()
        databaseFunctions().insertUser(
            id_account, first_name, last_name, username, password_encrypted.decode("utf-8")
        )
        return redirect(url_for('login'))

    flash('Your password and confirm passwords dont match! Please try again.')
    return redirect(url_for('create_user'))


# TODO: Implementar o sistema de login para verificar se existe
@app.route('/login')
def login():
    print()
    return render_template('login.html')


@app.route('/authentication', methods=['POST', ])
def authentication():
    databaseFunctions().createDatabase('user')
    username = request.form['username']
    password = request.form['password']

    if not databaseFunctions().verifyUsernameExists(username):
        user = databaseFunctions().verifyUsernameAndPwd(username)

        if bcrypt.checkpw(password.encode(), user[4].encode()):
            print('logged in')
            return redirect(url_for('index'))

        flash('Something went wrong, verify your account and password and try again')
        return redirect(url_for('login'))

    flash(f'Username {username} dont exist.')
    return redirect(url_for('login'))