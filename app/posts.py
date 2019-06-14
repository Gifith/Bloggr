from flask import Blueprint, render_template
from decorators.login import require_login
from decorators.admin import require_admin
from db.modele import Post
from db import db

PostAPI = Blueprint('PostApi', __name__, url_prefix="/posts")

@PostAPI.route("/list", methods=["GET"])
def get_postslist():
	return render_template('postslist.jinja', posts = Post.query.all())
#def get_postslist():
#    Liste = Posts.query.all()
#    for i in Liste:
#        print(i.titre, i.corpus,i.datecree, i.creator)
#    return Liste


@PostAPI.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
	return render_template('post.jinja', post = Post.query.get(post_id))
#def get_post(post_id):
#    Post = Posts.query.get(post_id)
#    print(Post.titre, Post.corpus,Post.datecree, Post.creator)
#    return Post


@PostAPI.route("/", methods=["POST"])
def create_post():
	title = request.get_json()['title']
	corpus = request.get_json()['corpus']
	imagelink = request.get_json()['imagelink']
	isActive = request.get_json()['isActive']
	post = Post(id = 3, titre = title, corpus = corpus, datecree = datetime.now(), datemodif = datetime.now(),creator = 3, Image = imagelink , active = isActive)
#def publish_post():

@PostAPI.route("/<int:post_id>", methods=["DELETE"])
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