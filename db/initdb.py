from .modele import User, Token, Post

import hashlib
from uuid import uuid4
from datetime import datetime
from db import db



def initialize():

    print "Before creating database..."

    db.create_all()

    print "After creating database..."

    sel = hashlib.sha256(uuid4().hex).hexdigest()
    hash1 = hashlib.sha256("{}{}".format('toto', sel)).hexdigest()

    user1 = User(username = 'premier', email = "premier@st.com", hash = hash1, sel = sel, role = 0, active = 1)

    sel = hashlib.sha256(uuid4().hex).hexdigest()
    hash1 = hashlib.sha256("{}{}".format('toto', sel)).hexdigest()
    
    user2 = User(username = 'second', email = "second@nd.com", hash = hash1, sel = sel, role = 1, active = 1)

    sel = hashlib.sha256(uuid4().hex).hexdigest()
    hash1 = hashlib.sha256("{}{}".format('toto', sel)).hexdigest()

    user3 = User(username = 'third', email = "third@rd.com", hash = hash1, sel = sel, role = 0, active = 1)


    
    token1 = Token(jwt = 'XXXXXXXXXXXXXXXXXXXXX', expiration = datetime(2022, 12, 14, 10, 0, 0))
    token2 = Token(jwt = 'YYYYYYYYYYYYYYYYYYYYY', expiration = datetime(2002, 3, 15, 10, 0, 0))
    token3 = Token(jwt = 'ZZZZZZZZZZZZZZZZZZZZZ', expiration = datetime(2222, 7, 10, 10, 0, 0))
    post1 = Post(titre = 'Un ours acrobate demoli', corpus = 'Apres son spectacle un ours acrobate se casse les 4 pattes en sautant du trapeze',datecree = datetime(2019, 3, 15, 10, 0, 0), datemodif = datetime(2019, 3, 15, 10, 0, 0),creator = 1 , Image = 'https://cap.img.pmdstatic.net/fit/http.3A.2F.2Fprd2-bone-image.2Es3-website-eu-west-1.2Eamazonaws.2Ecom.2Fcap.2F2018.2F11.2F19.2F152f6726-86b2-460f-8c42-1a679ff88a2e.2Ejpeg/750x375/background-color/ffffff/quality/70/debat-a-t-on-bien-fait-de-reintroduire-lours-dans-les-pyrenees-1316330.jpg' , active = True)
    post2 = Post(titre = 'Plus de pension alimentaire', corpus = 'La pension alimentaire est supprime en France des le 29 juillet',datecree = datetime(2019, 3, 17, 10, 0, 0), datemodif = datetime(2019, 3, 17, 10, 0, 0),creator = 2, Image = 'https://ichef.bbci.co.uk/news/660/cpsprodpb/174DC/production/_99325459_gettyimages-825838988.jpg' , active = True)
    post3 = Post(titre = 'Concours de Hula-Hoop', corpus = 'Jeannine est la gagnant du concours de Timilly sur Eure', datecree = datetime(2019, 3, 17, 10, 0, 0), datemodif = datetime(2019, 3, 17, 10, 0, 0),creator = 3, Image = 'https://bilder.hula-hoop-shop.eu/media/image/product/6141/md/hula-hoop-pour-les-enfants-colore-diamctre-80-75-70-65-60cm.jpg' , active = True)

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

    print "After Fixtures..."