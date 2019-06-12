from flask import Blueprint, render_template
from os.path import join, dirname, abspath

UsersAPI = Blueprint('UsersApi', __name__, url_prefix="/users")

@UsersAPI.route("/", methods=["GET"])
def get_users():
    return "Hello Users, hey ya"


@UsersAPI.route("/create", methods=["GET"])
def get_userform():
    return render_template('userform.jinja')



