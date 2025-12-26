# -*- coding: utf-8 -*-
from waitress import serve
from app import app

if __name__ == "__main__":
    print("⚡ Serveur Inventaire SaaS démarrage…")
    serve(app, host="0.0.0.0", port=5000)
