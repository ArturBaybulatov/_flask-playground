from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    private = db.Column(db.Boolean)
    share_count = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('notes', lazy=True))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
