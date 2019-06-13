from functools import wraps
from flask import g, request, redirect, abort
from db import db
from db.modele import Token

def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None: abort(401)
        elif g.role == 1: return f(*args, **kwargs)
        else: abort(403)
    return decorated_function


            