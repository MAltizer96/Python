import os
from pickle import FALSE

from flask import Flask,session,redirect,request,render_template
from flask_session import Session
from flask_mysqldb import MySQL

from helpers import login_required


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
print("mysql object", mysql.connection)
# create a cursor


#cursor.execute(''' IF NOT EXISTS (SELECT * FROM sys.tables WHERE NAME = 'ToDo) ''')



try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/')
def home_page():    
    return render_template("layout.html")

@app.route('/register')
def register():
    return 'not yet done'


if __name__ == '__main__':
    app.run()
