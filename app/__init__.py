from os.path import join, isfile, abspath, dirname, exists
from os import makedirs, remove
from flask import Flask, render_template

from .users import UsersAPI
from .tokens import TokensAPI
from .posts import PostAPI
from .app import app
from decorators.login import require_login
from decorators.admin import require_admin

from db.initdb import initialize
from db.antitoken import remove_old_tokens


app.register_blueprint(UsersAPI)
app.register_blueprint(PostAPI)
app.register_blueprint(TokensAPI)

@app.route("/")
def hello():
    return render_template('homepage.jinja')


rootdir = abspath(dirname(dirname(__file__)))
storagedir = join(rootdir,'storage') 
if not exists(storagedir):
    makedirs(storagedir)

if not isfile( join(storagedir, 'app.db') ):
    initialize()