from .modele import db, Token
from datetime import datetime

def remove_old_tokens():
    suppr = False    

    for tok in Token.query.all():
        if datetime.now() > tok.expiration:
            db.session.delete(tok)
            suppr = True

    if suppr == True:
        db.session.commit() 
