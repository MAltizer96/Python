import sqlite3

import click
from flask import current_app,g

def get_db():
    # checks if db is not in the g object
    if 'db' not in g:
        # creates a db object and connects to apps database 
        g.db = sqlite3.connect(
            # connects a connection to the apps database
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # tells db to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db=g.pop('db',None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # opens SQL commands realative to flaskr package
    with current_app.open_resource('schema.sql') as file:#hell
        db.executescript(file.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # tells flask to call that function when cleaning up
    app.teardown_appcontext(close_db)
    # addes a new command to be called with the flask command
    app.cli.add_command(init_db_command)