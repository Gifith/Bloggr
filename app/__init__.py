from os.path import join, isfile, abspath, dirname, exists
from os import makedirs, remove
from flask import Flask

from .users import UsersAPI
from .tokens import TokensAPI
from .posts import PostAPI
from .app import app
from db.modele import User, Token
from decorators.login import require_login
from decorators.admin import require_admin
import hashlib

from db import db

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


if not isfile( join(storagedir, 'app.db') ) and not exists(storagedir):
    makedirs(storagedir)
    db.create_all()

    sel = hashlib.sha512(uuid4())
    hash = hashlib.pbkdf2_hmac('sha256', 'toto', sel)
    user1 = User(id = '01', username = 'premier', email = "premier@st.com", hash = hash, sel = sel, role = 0, active = 1)
    sel = hashlib.sha512(uuid4())
    hash = hashlib.pbkdf2_hmac('sha256', 'toto', sel)
    user2 = User(id = '02', username = 'second', email = "second@nd.com", hash = hash, sel = sel, role = 1, active = 1)
    sel = hashlib.sha512(uuid4())
    hash = hashlib.pbkdf2_hmac('sha256', 'toto', sel)
    user3 = User(id = '03', username = 'third', email = "third@rd.com", hash = hash, sel = sel, role = 0, active = 1)


    
    token1 = Token(jwt = 'XXXXXXXXXXXXXXXXXXXXX', expiration = datetime(2022, 12, 14, 10, 0, 0))
    token2 = Token(jwt = 'YYYYYYYYYYYYYYYYYYYYY', expiration = datetime(2002, 3, 15, 10, 0, 0))
    token3 = Token(jwt = 'ZZZZZZZZZZZZZZZZZZZZZ', expiration = datetime(2222, 7, 10, 10, 0, 0))
    post1 = Post(id = 1, titre = 'Un ours acrobate demoli', corpus = 'Apres son spectacle un ours acrobate se casse les 4 pattes en sautant du trapeze',
        datecree = datetime(2019, 3, 15, 10, 0, 0), datemodif = datetime(2019, 3, 15, 10, 0, 0),creator = 1 , Image = 'https://cap.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Fcap.2F2018.2F11.2F19.2F152f6726-86b2-460f-8c42-1a679ff88a2e.2Ejpeg/750x375/background-color/ffffff/quality/70/debat-a-t-on-bien-fait-de-reintroduire-lours-dans-les-pyrenees-1316330.jpg' , active = True)
    post2 = Post(id = 2, titre = 'Plus de pension alimentaire', corpus = 'La pension alimentaire est supprime en France des le 29 juillet',
        datecree = datetime(2019, 3, 17, 10, 0, 0), datemodif = datetime(2019, 3, 17, 10, 0, 0),creator = 2, Image = 'https://ichef.bbci.co.uk/news/660/cpsprodpb/174DC/production/_99325459_gettyimages-825838988.jpg' , active = True)
    post3 = Post(id = 3, titre = 'Concours de Hula-Hoop', corpus = 'Jeannine est la gagnant du concours de Timilly sur Eure',
        datecree = datetime(2019, 3, 17, 10, 0, 0), datemodif = datetime(2019, 3, 17, 10, 0, 0),creator = 3, Image = 'https://bilder.hula-hoop-shop.eu/media/image/product/6141/md/hula-hoop-pour-les-enfants-colore-diamctre-80-75-70-65-60cm.jpg' , active = True)



    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(token1)
    db.session.add(token2)
    db.session.add(token3)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.commit()
        
else:
    if isfile( join(storagedir, 'app.db') ):
        remove(join(storagedir, 'app.db'))

db.create_all()

user1 = User(id = '01', username = 'premier', email = "premier@st.com", hash = '721GBBH1', sel = 'IJZNhnahzb', role = 0, active = 1)
user2 = User(id = '02', username = 'second', email = "second@nd.com", hash = 'dzah124NDUI7', sel = 'age2d2R3', role = True, active = 1)
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

