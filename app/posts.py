from flask import Blueprint
from db.modele import Post
from db import db

PostAPI = Blueprint('PostApi', __name__, url_prefix="/posts")

@PostAPI.route("/", methods=["GET"])
def get_posts():
    Liste = Posts.query.all()
    for i in Liste:
        print(i.titre, i.corpus,i.datecree, i.creator)
    return Liste

@PostAPI.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    Post = Posts.query.filter(Posts.id == post_id).first()
    print(Post.titre, Post.corpus,Post.datecree, Post.creator)
    return Post

@PostAPI.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
	if countPost(post_id) > 0 :
		print('post exists, delete')
		db.session.query(Post).filter(Post.id == post_id ).delete()
		db.session.commit()
		return Response(redirect((url_for('PostApi.get_posts'))),status=204, mimetype='application/json')
	else:
		return Response(status=410, mimetype='application/json')

def countPost(post_id):
	return db.session.query(Token).filter( Post.id == post_id ).count()