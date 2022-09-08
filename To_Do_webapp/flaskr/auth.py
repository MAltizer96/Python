import functools
from sqlite3 import IntegrityError

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from . import helpers
# create blueprint named auth
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":      
        # set variables
        username = request.form.get("username")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirm_password")  
        db = get_db()
        error = None  

        # confirm passwords match
        if password != confirmPassword:        
            error = "Passwords Dont Match"
        
        if not password:
            error = "No Password Provided"
        # checks username for errors
        if not username:
            error = "No Username Provided"
       
        if error is None:
            try:
                # adds users to database
                db.execute("INSERT INTO users (username, password) VALUES (?,?)",(username,generate_password_hash(password)))
                db.commit()               
            except db.IntegrityError:
                # name taken
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        # set variables
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        error = None
        # check for provided username and password
        if not username:
            error = 'Username Not Provided'
        if not password:
            error = 'Password Not provided'
        
        if error is None:       
            # get the user from the database     
            user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            # check if user exists and password is correct            
            if user is None or not check_password_hash(user['password'],password):
                error = 'Incorrect Username or Password'

            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')
            
bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_logged_in_user():
    # gets user_id if set
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        # gets users form database and stores it
        g.user = get_db().execute('SELECT * FROM users WHERE id = ?', user_id).fetchone        

def login_required(view):  
    # wraps around the view that was passed in  
    @functools.wraps(view)
    # function to wrap around the view
    def wrapped_view(**kwargs):
        # checks for user
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        # return the new wraped view
        return view(**kwargs)
    return wrapped_view