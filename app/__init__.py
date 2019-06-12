from os.path import join, isfile, abspath, dirname, exists
from os import makedirs, remove
from flask import Flask

from .users import UsersAPI
from .tokens import TokensAPI
from .posts import PostAPI
from .app import app
from db.modele import User, Token

from db import db

from datetime import date, datetime

from db.antitoken import remove_old_tokens


app.register_blueprint(UsersAPI)
app.register_blueprint(PostAPI)
app.register_blueprint(TokensAPI)

@app.route("/")
def hello():
    return "Hello World !"

rootdir = abspath(dirname(dirname(__file__)))
storagedir = join(rootdir,'storage') 


if not isfile( join(storagedir, 'app.db') ) and not exists(storagedir):
    makedirs(storagedir)
    db.create_all()
    user1 = User(id = '01', username = 'premier', email = "premier@st.com", hash = '721GBBH1', sel = 'IJZNhnahzb', role = 0, active = 1)
    user2 = User(id = '02', username = 'second', email = "second@nd.com", hash = 'dzah124NDUI7', sel = 'age2d2R3', role = 0, active = 1)
    user3 = User(id = '03', username = 'third', email = "third@rd.com", hash = 'gazr7nd7', sel = 'az928Klm2', role = 0, active = 1)
    token1 = Token(jwt = 'XXXXXXXXXXXXXXXXXXXXX', expiration = datetime(2022, 12, 14, 10, 0, 0))
    token2 = Token(jwt = 'YYYYYYYYYYYYYYYYYYYYY', expiration = datetime(2002, 3, 15, 10, 0, 0))
    token3 = Token(jwt = 'ZZZZZZZZZZZZZZZZZZZZZ', expiration = datetime(2222, 7, 10, 10, 0, 0))

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(token1)
    db.session.add(token2)
    db.session.add(token3)
    db.session.commit()
        
else:
    if isfile( join(storagedir, 'app.db') ):
        remove(join(storagedir, 'app.db'))

db.create_all()

user1 = User(id = '01', username = 'premier', email = "premier@st.com", hash = '721GBBH1', sel = 'IJZNhnahzb', role = 0, active = 1)
user2 = User(id = '02', username = 'second', email = "second@nd.com", hash = 'dzah124NDUI7', sel = 'age2d2R3', role = 0, active = 1)
user3 = User(id = '03', username = 'third', email = "third@rd.com", hash = 'gazr7nd7', sel = 'az928Klm2', role = 0, active = 1)
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.commit()


print("Utilisateurs:")
print(User.query.all())

print("Tokens avant:")
print(Token.query.all())

remove_old_tokens()

print("Tokens apres:")
print(Token.query.all())

Liste = User.query.all()
for i in Liste:
    print(i.id, i.username, i.email)

