from flask import render_template, redirect, url_for, request
import hashlib
import bcrypt

from helpers.database import databaseFunctions
from app import app


@app.route('/create-user')
def create_user():
    return render_template('create_user.html')



@app.route('/creatinguser', methods=['POST',])
def creating_user():
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    databaseFunctions().createDatabase('user')

    return redirect(url_for('create_user'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authentication')
def authentication():
    return redirect('index')