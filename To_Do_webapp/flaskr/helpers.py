from flask import g, request, redirect, url_for, render_template

def login_required(f):   
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def error(message, code=400):
    return render_template("error.html", top=code,bottom=message)