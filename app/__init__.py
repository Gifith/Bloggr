from os.path import join, isfile, abspath, dirname, exists
from os import makedirs, remove
from flask import Flask

from .users import UsersAPI
from .tokens import TokensAPI
from .posts import PostAPI
from .app import app
from db.modele import User, Token, Post
from decorators.login import require_login
from decorators.admin import require_admin
import hashlib
from uuid import uuid4

from db import db

from db.initdb import initialize

from datetime import date, datetime

from db.antitoken import remove_old_tokens


app.register_blueprint(UsersAPI)
app.register_blueprint(PostAPI)
app.register_blueprint(TokensAPI)

@app.route("/")
def hello():
    return "Hello World !"

@app.route("/logged")
@require_login
def loggedin():
    return "You are logged"

@app.route("/admin")
@require_login
@require_admin
def admin():
    return "Admin connected"


rootdir = abspath(dirname(dirname(__file__)))
storagedir = join(rootdir,'storage') 
if not exists(storagedir):
    makedirs(storagedir)

if not isfile( join(storagedir, 'app.db') ):
    initialize()