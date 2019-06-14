from flask import Blueprint, render_template, request, Response, jsonify, redirect, url_for
from datetime import datetime
from decorators.login import require_login
from decorators.admin import require_admin
from db.modele import Post
from db import db

PostAPI = Blueprint('PostApi', __name__, url_prefix="/posts")

@PostAPI.route("/", methods=["GET"])
def get_users():
    return "Accueil posts : go to /list"

@PostAPI.route("/list", methods=["GET"])
def get_postslist():
	if request.is_json :
		return jsonify(json_list = Post.query.with_entities(Post.title, Post.corpus))
	else:
		return render_template('postslist.jinja', posts = Post.query.all())
#def get_postslist():
#    Liste = Posts.query.all()
#    for i in Liste:
#        print(i.titre, i.corpus,i.datecree, i.creator)
#    return Liste


@PostAPI.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
	if request.is_json :
		return jsonify(json_list = Post.query.filter(Post.id == post_id).first().with_entities(Post.title, Post.corpus))
	else:
		return render_template('post.jinja', post = Post.query.get(post_id))
#def get_post(post_id):
#    Post = Posts.query.get(post_id)
#    print(Post.titre, Post.corpus,Post.datecree, Post.creator)
#    return Post


@PostAPI.route("/create", methods=["GET"])
def create_post():
		return render_template('createpost.jinja')

@PostAPI.route("/", methods=["POST"])
def post_create():
	print("---------------")
	print(request.get_json())
	print("---------------")
	title = request.get_json()['title']
	corpus = request.get_json()['corpus']
	imagelink = request.get_json()['imagelink']
	isActive = request.get_json()['isActive']
	print(title+" "+corpus+" "+imagelink)
	post = Post(titre = title, corpus = corpus, datecree = datetime.now(), datemodif = datetime.now(),creator = 3, Image = imagelink , active = True)
	db.session.add(post)
	db.session.commit()
	return Response(redirect((url_for('PostApi.get_postslist'))),status=204, mimetype='application/json')

@PostAPI.route("/<int:post_id>", methods=["DELETE"])
@require_login
@require_admin
def delete_post(post_id):
	if countPost(post_id) > 0 :
		print('post exists, delete (active = 0)')
		db.session.update(Post).where(users.c.id==post_id).values(active=False)
		#db.session.query(Post).filter(Post.id == post_id ).delete()
		db.session.commit()
		return Response(redirect((url_for('PostApi.get_postslist'))),status=204, mimetype='application/json')
	else:
		return Response(status=410, mimetype='application/json')

def countPost(post_id):
	return db.session.query(Token).filter( Post.id == post_id ).count()