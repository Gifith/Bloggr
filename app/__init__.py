from os.path import join, isfile, abspath, dirname
from flask import Flask

from .users import UsersAPI
from .tokens import TokensAPI
from .posts import PostAPI


app = Flask(__name__)

app.register_blueprint(UsersAPI)
app.register_blueprint(PostAPI)
app.register_blueprint(TokensAPI)

@app.route("/")
def hello():
    return "Hello World !"

from db.modele import db

if isfile( join(abspath(dirname(dirname(__file__))), 'storage', 'app.db') ) == False:
    db.create_all()
else:
    print("Base de donnees presente")