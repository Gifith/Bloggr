from flask import Blueprint,request,Response,jsonify, redirect, url_for
from datetime import datetime
import jwt
import random
import hashlib
from db.modele import Token, User
from db import db
###########################################################
TokensAPI = Blueprint('TokensApi', __name__, url_prefix="/tokens")

##TO DELETE AFTER TESTS
@TokensAPI.route("/", methods=["GET"])
def displayTokens():
    Liste = Token.query.all()
    for i in Liste:
        print(i.jwt, i.expiration)
    return jsonify("watch the logs")

@TokensAPI.route("/", methods=["POST"])
def login():
    if not request.form['email'] or not request.form['password'] or not request.form['username']:
        return redirect("../users/create", code=400)
    else:
        #u = request.get_json()['username']
        #pw = request.get_json()['password']
        u = request.form['username']
        pw = request.form['password']

        tokenVal = jwt.encode({u:pw}, 'A python blogging platform', algorithm='HS256')

        if countToken(tokenVal) == 0:

            info = User.query.filter_by(username=u).first()
            if info is None:
                return redirect('UsersApi.get_userform', code=401)
            else:
                #hash = hashlib.pbkdf2_hmac('sha256', pw, info.salt)
                if pw == info.hash:
                    tokObjToAdd = Token(jwt=tokenVal,expiration=datetime.now())
                    db.session.add(tokObjToAdd)
                    db.session.commit()
                    return redirect(url_for('UsersApi.get_users'))
        else:
            db.session.query(Token).filter_by(jwt=tokenVal).update(dict(expiration=datetime.now()))
            db.session.commit()
            return jsonify({'token': tokenVal})

@TokensAPI.route("/", methods=["DELETE"])
def logout():
    tok = request.headers.get('Authorization').split(' ')
    tok = tok[1]
    if countToken(tok)>0 :
        print('token exists, delete')
        db.session.query(Token).filter(Token.jwt == tok).delete()
        db.session.commit()
        return Response(status=204, mimetype='application/json')
    else:
        return Response(status=410, mimetype='application/json')

def countToken(tokenVal):
    return db.session.query(Token).filter( Token.jwt==tokenVal ).count()

#1xx Informational
#100 Continue
#101 Switching Protocols
#102 Processing

#2xx Success
#200 OK
#201 Created
#202 Accepted
#203 Non-authoritative Information
#204 No Content
#205 Reset Content
#206 Partial Content
#207 Multi-Status
#208 Already Reported
#226 IM Used

#3xx Redirection
#300 Multiple Choices
#301 Moved Permanently
#302 Found
#303 See Other
#304 Not Modified
#305 Use Proxy
#307 Temporary Redirect
#308 Permanent Redirect

#4xx Client Error
#400 Bad Request
#401 Unauthorized
#402 Payment Required
#403 Forbidden
#404 Not Found
#405 Method Not Allowed
#406 Not Acceptable
#407 Proxy Authentication Required
#408 Request Timeout
#409 Conflict
#410 Gone
#411 Length Required
#412 Precondition Failed
#413 Payload Too Large
#414 Request-URI Too Long
#415 Unsupported Media Type
#416 Requested Range Not Satisfiable
#417 Expectation Failed
#418 I'm a teapot
#421 Misdirected Request
#422 Unprocessable Entity
#423 Locked
#424 Failed Dependency
#426 Upgrade Required
#428 Precondition Required
#429 Too Many Requests
#431 Request Header Fields Too Large
#444 Connection Closed Without Response
#451 Unavailable For Legal Reasons
#499 Client Closed Request

#5xx Server Error
#500 Internal Server Error
#501 Not Implemented
#502 Bad Gateway
#503 Service Unavailable
#504 Gateway Timeout
#505 HTTP Version Not Supported
#506 Variant Also Negotiates
#507 Insufficient Storage
#508 Loop Detected
#510 Not Extended
#511 Network Authentication Required
#599 Network Connect Timeout Error