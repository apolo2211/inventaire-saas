# -*- coding: utf-8 -*-
# run_waitress.py
# ⚡ Serveur backend Inventaire SaaS avec Waitress

from waitress import serve
from app import app

if __name__ == "__main__":
    print("⚡ Serveur Inventaire SaaS démarrage en cours…")
    # Écoute sur toutes les interfaces pour le cloud
    serve(app, host="0.0.0.0", port=5000)
