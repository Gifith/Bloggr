from flask import Blueprint, render_template, request, redirect, abort, url_for
from os.path import join, dirname, abspath
from decorators.login import require_login
from decorators.admin import require_admin
from db.modele import User, ResetToken
from db import db
import time
from uuid import uuid4
import hashlib
from datetime import datetime

UsersAPI = Blueprint('UsersApi', __name__, url_prefix="/users")

@UsersAPI.route("/", methods=["GET"])
def get_users():
    return render_template('userspage.jinja')


@UsersAPI.route("/register", methods=["GET"])
@require_login
@require_admin
def set_user():
    return render_template('register.jinja')


@UsersAPI.route("/login", methods=["GET"])
def get_userform():
    return render_template('userform.jinja')


@UsersAPI.route("/list", methods=["GET"])
@require_login
@require_admin
def get_userlist():
    if request.is_json :
        return jsonify(json_list = User.query.with_entities(User.email, User.username))
    else:
        return render_template('userslist.jinja', users = User.query.all())


@UsersAPI.route("/<int:user_id>", methods=["GET"])
@require_login
@require_admin
def get_user(user_id):
    if request.is_json :
        return jsonify(json_list = User.query.filter(User.id == user_id).first().with_entities(User.email, User.username))
    else:
        return render_template('users.jinja', user = User.query.get(user_id))


@UsersAPI.route("/saving", methods=["POST"])
@require_login
def save_user():
    if request.is_json:
        m = request.json['email']
        u = request.json['username']
        pw = request.json['password']
    else:
        m = request.form['email']
        u = request.form['username']
        pw = request.form['password']

    ucheck = User.query.filter( User.username == u ).count()
    mcheck = User.query.filter( User.email == m ).count()
    if ucheck == 0 and mcheck == 0:
        sel = hashlib.sha256(uuid4().hex).hexdigest()
        hash = hashlib.sha256("{}{}".format(pw, sel)).hexdigest()
        user = User(username = u, email = m, hash = hash, sel = sel, role = 0, active = 1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('UsersApi.get_userlist'))
    else:
        abort(422)


@UsersAPI.route("/reset", methods=['GET','POST'])
def resetpass():
    if request.method == "GET":
        return render_template('resetpass.jinja')
    elif request.method == "POST":
        if request.is_json :
            usern = request.get_json()['username']
            mail = request.get_json()['email']
            json = True
        else:
            usern = request.form['username']
            mail = request.form['email']
            json = False

        info = User.query.filter(User.username == usern, User.email == mail).first()

        if info is None:
            abort(422)
        else:
            uniqueid = hashlib.sha256("{}{}".format(usern, hashlib.sha256(uuid4().hex).hexdigest())).hexdigest()
            exp = datetime.now()
            token = ResetToken(token = uniqueid, expiration = exp, user = usern)
            db.session.add(token)
            db.session.commit()
            return render_template('resetconfirm.jinja', token = uniqueid)


#@UsersAPI.route("/falsemail", methods=['POST'])
#def resetmail():
            

@UsersAPI.route("/passreset/<string:token>", methods=["GET","POST"])
def token_password(token):

    check = ResetToken.query.filter(ResetToken.token == token).first()
    if check is None:
        abort(404)
    else:
        if request.method == "GET":
            return render_template('newpass.jinja')
        if request.method == "POST":

            u = User.query.filter_by(username=check.user).first()
            u.hash = hashlib.sha256("{}{}".format(request.form['pass'], u.sel)).hexdigest()
            db.session.commit()
            return redirect(url_for('UsersApi.get_userform'))




@UsersAPI.route("/<int:user_id>", methods=["DELETE"])
@require_login
@require_admin
def delete_user(user_id):
    if countUser(user_id) > 0 :
        print('user exists, delete (active = 0)')
        db.session.update(User).where(User.id==user_id).values(active=False)
        #db.session.query(User).filter(User.id == user_id ).delete()
        db.session.commit()
        return Response(redirect((url_for('PostApi.get_postslist'))),status=204, mimetype='application/json')
    else:
        return Response(status=410, mimetype='application/json')

def countUser(user_id):
    return db.session.query(Token).filter( User.id == user_id ).count()

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