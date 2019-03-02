from flask_sqlalchemy import SQLAlchemy

from . import setup as app

db = SQLAlchemy(app)