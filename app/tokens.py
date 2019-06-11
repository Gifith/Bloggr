from flask import Blueprint,request, jsonify
import jwt

TokensAPI = Blueprint('TokensApi', __name__, url_prefix="/tokens")


@TokensAPI.route("/", methods=["POST"])
def login():
    givenU = request.get_json()['username']
    givenPW = request.get_json()['password']
    return jsonify(makeToken(givenU, givenPW))  

@TokensAPI.route("/", methods=["DELETE"])
def logout():
    return "logout ok"

def makeToken(givenU,givenPW):
    key = 'secret'
    encoded = jwt.encode({givenU:givenPW}, key, algorithm='HS256')
    return encoded