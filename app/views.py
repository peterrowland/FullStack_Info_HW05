# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os, sys
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['username']
        return render_template('survey.html', username=username)
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST']) # You need to specify something here for the function to get requests
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['email'] = request.form['email']
    else:
        session['username'] = request.args['username']
        session['email'] = request.args['email']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    username = ''
    email = ''
    if ('username' in session):
        username = session.get('username')
        surveyResponse = {}
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['vacation'] = request.form.get('vacation')
        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')
        print(surveyResponse)
        return render_template('results.html', name = username, surveyResponse = surveyResponse )
    else:
        return render_template('login.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
