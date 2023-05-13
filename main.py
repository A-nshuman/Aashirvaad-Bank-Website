from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anshuman2006",
    database="bankdata"
)

# Login page route
@app.route('/login')
def login():
    return render_template('login2.html')

# Register page route
@app.route('/register')
def register():
    return render_template('register2.html')

# Registration form submit route
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    username = request.form['username']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    # Insert form data into MySQL database
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, firstname, lastname, email, password) VALUES (%s, %s, %s, %s, %s)"
    val = (username, firstname, lastname, email, password)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

    return redirect(url_for('login'))

# Login form submit route
@app.route('/auth', methods=['POST'])
def auth():
    # Get form data
    username = request.form['username']
    password = request.form['password']

    # Check if user exists in MySQL database
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()
    mycursor.close()

    # If user exists, redirect to dashboard page
    if user:
        return render_template('dashboard.html', first_name=user[2], last_name=user[3])
    # If user does not exist, redirect to login page
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
