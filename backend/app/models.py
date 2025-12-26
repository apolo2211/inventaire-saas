# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Admin / Staff

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, default=0)
    value = db.Column(db.Float, default=0.0)
    code_unique = db.Column(db.String(50), unique=True)

class Movement(db.Model):
    __tablename__ = "movements"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quantity_change = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
