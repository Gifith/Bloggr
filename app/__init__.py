from os.path import join, isfile, abspath, dirname, exists
from os import makedirs
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

from db.modele import db, User

if isfile( join(abspath(dirname(dirname(__file__))), 'storage', 'app.db') ) == False:
    if not exists(join(abspath(dirname(dirname(__file__))), 'storage')):
        makedirs(join(abspath(dirname(dirname(__file__))), 'storage'))
    db.create_all()
    user1 = User(id = '01', username = 'premier', email = "premier@st.com", hash = '721GBBH1', sel = 'IJZNhnahzb', role = 0, active = 1)
    user2 = User(id = '02', username = 'second', email = "second@nd.com", hash = 'dzah124NDUI7', sel = 'age2d2R3', role = 0, active = 1)
    user3 = User(id = '03', username = 'third', email = "third@rd.com", hash = 'gazr7nd7', sel = 'az928Klm2', role = 0, active = 1)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
        
else:
    print("Base de donnees presente")


print("Utilisateurs:")
print(User.query.all())