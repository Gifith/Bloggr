from flask import Blueprint

PostAPI = Blueprint('PostApi', __name__, url_prefix="/posts")

@PostAPI.route("/", methods=["GET"])
def get_posts():
    return "Hello Posts"