# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

# Création d'un utilisateur
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'Staff')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username déjà utilisé"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email déjà utilisé"}), 400

    hashed_pw = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_pw, role=role)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "Utilisateur créé avec succès"}), 201

# Connexion utilisateur
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Nom d'utilisateur ou mot de passe incorrect"}), 401

    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify({"access_token": access_token}), 200
