from functools import wraps
from flask import g, request, redirect, abort
from db import db
from db.modele import Token, User
import datetime
import jwt

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get("token") is None:
            if request.headers.get('Authorization').split(' ')[1] is None:
                print("pas de cookie")
                abort(401)
            else:
                tok = request.headers.get('Authorization').split(' ')[1]
        else:
            tok = request.cookies.get("token")

        info = Token.query.filter_by(jwt=tok).first()
        if info is None:
            print("pas de cookie dans la base")
            abort(401)
        elif  (datetime.datetime.now() - info.expiration).seconds > 7200:
            print("cookie expire")
            abort(401)
        else:
            user = jwt.decode(tok, 'A python blogging platform', algorithm='HS256')['u']
            user = User.query.filter_by(username = user).first()
            if user is None:
                abort(401)
            g.user = user
            g.role = user.role
            print("Login OK")
            return f(*args, **kwargs)
    return decorated_function