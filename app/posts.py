from flask import Blueprint, render_template, request, Response, jsonify, redirect, url_for, g
from datetime import datetime
from decorators.login import require_login
from decorators.admin import require_admin
from db.modele import Post,Tag
from db import db
import json as jsonLib

PostAPI = Blueprint('PostApi', __name__, url_prefix="/posts")

@PostAPI.route("/", methods=["GET"])
def get_users():
    return render_template("postspage.jinja")

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
@require_login
def create_post():
		return render_template('createpost.jinja')

@PostAPI.route("/", methods=["POST"])
@require_login
def post_create():
	json = request.get_json()
	title = json['title']
	corpus = json['corpus']
	imagelink = json['imagelink']
	tags = json['tags']
	isActive = json['isActive']
	print(title+" "+corpus+" "+imagelink)
	post = Post(titre = title, corpus = corpus, datecree = datetime.now(), datemodif = datetime.now(),creator = g.user.id, Image = imagelink , active = True)
	for tag in extract_tags(tags):
		post.tags.append(tag)
	db.session.add(post)
	db.session.commit()
	db.session.flush()
	#assoc_tags_to_post(extract_tags(tags),Post.id)
	return jsonify(dict(
		id=post.id,
		titre=post.titre,
		corpus=post.corpus,
		datecree=post.datecree,
		datemodif=post.datemodif
	)), 201

@PostAPI.route("/<int:post_id>", methods=["DELETE"])
@require_login
@require_admin
def delete_post(post_id):
	if countPost(post_id) > 0 :
		print('post exists, delete (active = 0)')
		db.session.update(Post).where(Post.id==post_id).values(active=False)
		#db.session.query(Post).filter(Post.id == post_id ).delete()
		db.session.commit()
		return Response(redirect((url_for('PostApi.get_postslist'))),status=204, mimetype='application/json')
	else:
		return Response(status=410, mimetype='application/json')

def countPost(post_id):
	return db.session.query(Token).filter( Post.id == post_id ).count()

def extract_tags(tags):
	return [ Tag(titre=tag) for tag in tags.strip().split(',') ]