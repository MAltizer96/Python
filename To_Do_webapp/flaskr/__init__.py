import os

from flask import Flask,session,redirect,request,render_template
from flask_session import Session

from . import helpers, db, auth,lists

def create_app(test_config=None):        
    # create and configure the app
    app = Flask(__name__,instance_relative_config=True)

    # set mapping for key
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # loads the instance config, if it exisits, when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        # loads test config
        app.config.from_mapping(test_config)

    # auto reload templates
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # config sessions
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    Session(app)

    # initalize database
    db.init_app(app)

    #register blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(lists.bp)
    app.add_url_rule('/',endpoint='index') 

 
    # makes sure the path instance path exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        
    return app



