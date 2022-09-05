import os
from pickle import FALSE

from flask import Flask,session,redirect,request,render_template
from flask_session import Session
from flask_mysqldb import MySQL

from helpers import login_required,error


# create and configure the app
app = Flask(__name__)

# auto reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# config sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# config database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config["MYSQL_PASSWORD"] = 'Password'
app.config['MYSQL_DB'] = 'to_do_webapp'
mysql = MySQL(app)
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.route('/')
def home_page():    
    
    return render_template("index.html")
    

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "GET":
        print("ran")
        return render_template("register.html")
    # post
    username = request.form.get("username")
    password = request.form.get("password")
    confirmPassword = request.form.get("confirm_password")
    # confirm passwords match
    if password != confirmPassword:        
        return error("Passwords Dont Match")
    # create cursor object
    curser = mysql.connection.cursor()
     # check database for username  
    checkForUser = curser.execute(""" SELECT username FROM users WHERE username = ?""", username )
    if checkForUser != None:
        return error("Username Already Taken")
    

    curser.execute(""" INSERT INTO users (username, hashword) VALUE( ?, ?) """, )
    return 'not yet done'


if __name__ == '__main__':
    app.run()
