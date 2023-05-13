# import mysql.connector
# from mysql.connector import errorcode
# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re

# app = Flask(__name__)

# # Change this to your secret key (can be anything, it's for extra protection)
# # app.secret_key = 'your secret key'

# # Enter your database connection details below
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Anshuman2006'
# app.config['MYSQL_DB'] = 'bankdata'

# # Intialize MySQL
# mysql = MySQL(app)

# # http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
# @app.route('/login 2', methods=['GET', 'POST'])
# def login():
#     # Output message if something goes wrong...
#     msg = ''
#     # Check if "username" and "password" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']
#         # Check if account exists using MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
#         # Fetch one record and return result
#         account = cursor.fetchone()
#         # If account exists in accounts table in out database
#         if account:
#             # Create session data, we can access this data in other routes
#             session['loggedin'] = True
#             session['id'] = account['id']
#             session['username'] = account['username']
#             # Redirect to home page
#             return redirect(url_for('dashboard'))
#         else:
#             # Account doesnt exist or username/password incorrect
#             msg = 'Incorrect username/password!'
#     # Show the login form with message (if any)
#     return render_template('index.html', msg=msg)

# # http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
# @app.route('Aashirvaas Bank Website/register 2', methods=['GET', 'POST'])
# def register():
#     # Output message if something goes wrong...
#     msg = ''
#     # Check if "username", "password" and "email" POST requests exist (user submitted form)
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         password = request.form['password']

#         # Check if account exists using MySQL
#         # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         # cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
#         # account = cursor.fetchone()
#         # If account exists show error and validation checks
#         # if account:
#         #     msg = 'Account already exists!'
#         # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#         #     msg = 'Invalid email address!'
#         # elif not re.match(r'[A-Za-z0-9]+', username):
#         #     msg = 'Username must contain only characters and numbers!'
#         # elif not username or not password or not email or not firstname or not lastname:
#         #     msg = 'Please fill out the form!'
#         # else:
#             # Account doesnt exists and the form data is valid, now insert new account into accounts table
#             # cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s)', (username, firstname, lastname, email, password,))
#             # mysql.connection.commit()
#             # msg = 'You have successfully registered!'

#     # elif request.method == 'POST':
#         # Form is empty... (no POST data)
#         # msg = 'Please fill out the form!'
#     # Show registration form with message (if any)
#     # return render_template('register 2.html', msg=msg)


# # http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
# # @app.route('dashboard')
# # def profile():
#     # Check if user is loggedin
#     # if 'loggedin' in session:
#         # We need all the account info for the user so we can display it on the profile page
#         # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         # cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
#         # account = cursor.fetchone()
#         # Show the profile page with account info
#         # return render_template('dashboard.html', account=account)
#     # User is not loggedin redirect to login page
#     # return redirect(url_for('login 2'))


# # cnx = mysql.connector.connect(user='root', 
# #                               password='Anshuman2006',
# #                               host='localhost')

# # cursor = cnx.cursor()