from .db import db
import hashlib

TagPostIndex = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.Text, nullable=False)
    sel = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_valid_pw(self, pw):
        sel = self.sel
        hash2 = hashlib.sha256("{}{}".format(pw, sel)).hexdigest()
        print(self.hash)
        print(hash2)
        return self.hash == hash2


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text, nullable=False)
    corpus = db.Column(db.Text, nullable=False)
    datecree = db.Column(db.DateTime, nullable=False)
    datemodif = db.Column(db.DateTime, nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Image = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    TagPostIndex = db.relationship('Tag', secondary=TagPostIndex, lazy='subquery',
        backref=db.backref('post', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.titre

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.titre


class Token(db.Model):
    jwt = db.Column(db.Text, primary_key=True)
    expiration = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<Token %r>' % self.jwt
