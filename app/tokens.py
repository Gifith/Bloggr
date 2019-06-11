from flask import Blueprint

TokensAPI = Blueprint('TokensApi', __name__, url_prefix="/tokens")

@TokensAPI.route("/", methods=["GET"])
def get_tokens():
    return "Hello Token !!"