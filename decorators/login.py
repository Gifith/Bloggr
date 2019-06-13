from functools import wraps
from flask import g, request, redirect, abort
from db import db
from db.modele import Token
import datetime

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.cookies.get("token") is None:
            abort(401)
        else:
            info = Token.query.filter_by(jwt=request.cookies.get("token")).first()
            if info is None:
                abort(401)
            elif  (datetime.datetime.combine(datetime.date(2019,6,5), datetime.datetime.min.time()) - info.expiration).seconds > 7200:
                abort(401)
            else:
                return f(*args, **kwargs)
    return decorated_function


            