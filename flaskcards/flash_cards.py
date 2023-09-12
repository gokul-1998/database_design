from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flash_cards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.String(100), nullable=False)
    # cards=db.relationship('Card', backref='user', lazy=True)

class Deck(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags=db.Column(db.String(100), nullable=False)
    date_created=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_reviewed=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    score=db.Column(db.Integer, nullable=False, default=0)

    # cards=db.relationship('Card', backref='deck', lazy=True)

class Card(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(100), nullable=False)
    answer=db.Column(db.String(100), nullable=False)
    deck_id=db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=False)
    date_created=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return '<User %r>' % self.name