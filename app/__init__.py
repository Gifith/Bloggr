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