from db.modele import db, Token

def TestTokenOld(lesTokens):
    suppr = false

    for tok in lesTokens:
        if datetime.datetime.now() > tok.expiration:
            # db.session.delete(me)
            print tok.jwt
            suppr = true

    if suppr == true:
        db.session.commit() 


