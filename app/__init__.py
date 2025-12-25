# -*- coding: utf-8 -*-
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend Inventaire SaaS OK"

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/test")
def test():
    return jsonify({"message": "Test réussi !"})
