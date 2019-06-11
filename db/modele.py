from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, abspath, dirname

from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(abspath(dirname(dirname(__file__))), 'storage', 'app.db')
db = SQLAlchemy(app)

print app.config['SQLALCHEMY_DATABASE_URI']

TagPostIndex = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hash = db.Column(db.String(256), nullable=False)
    sel = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.Text, unique=True, nullable=False)
    corpus = db.Column(db.Text, nullable=False)
    datecree = db.Column(db.DateTime, nullable=False)
    datemodif = db.Column(db.DateTime, nullable=False)
    creator = db.Column(db.String(80), db.ForeignKey('user.id'), nullable=False)
    Image = db.Column(db.String(256), unique=True, nullable=False)
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