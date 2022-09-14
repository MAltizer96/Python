from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

import datetime
# create blueprint
bp = Blueprint('list',__name__,)

# default route of webapp
@bp.route('/')
def index():    
    try:
        # if user is in a session (logged in)
        userID = session['user_id']        
        list = getListOfToDo(userID)
        return render_template('index.html',to_do_list=list)
    except:         
        return render_template('index.html')

    

@bp.route('/create', methods=["POST"])
@login_required
def create():    
    # set variables        
    itemToDo = request.form.get("ToDo")    
    db = get_db()
    error = None
    userID = session['user_id']
    # verifys user input
    if not itemToDo:
        error = "Please Provide a list of things to do"  
     
    if error is None:          
        try:
            # inserts todo item into database
            currentDateTime = datetime.datetime.now()
            print("currentDateTime = ", currentDateTime)
            db.execute('INSERT INTO lists (user_id, todo,time_stamp) VALUES (?,?,?)', (userID, itemToDo,currentDateTime))
            db.commit()
        except:
            # any errors flash that it failed            
            error = "failed to submit to database"            
        else:
            # return to home page
            return redirect(url_for('index'))
    flash(error)
    return redirect(url_for('index'))

@bp.route('/<int:id>/delete', methods=["POST"])
@login_required
def delete(id):
    db = get_db()
    error = None 
    try:
        db.execute('DELETE FROM lists WHERE id = ?',(id,))
        db.commit()
    except:
        error="failed to delete try again"
        flash(error)
    return redirect(url_for('index'))
        
    
    
    

def getListOfToDo(userID):
    db = get_db()    
    toDos = db.execute('SELECT todo,id FROM lists WHERE user_id = ?',(userID,)).fetchall()
    # for row in toDos:
    #     print(f"id = {row['id']}, todo = {row['todo']}" )
    return toDos     