from app.app import app
from os.path import join, abspath, dirname
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(abspath(dirname(dirname(__file__))), 'storage', 'app.db')
db = SQLAlchemy(app)
print app.config['SQLALCHEMY_DATABASE_URI']