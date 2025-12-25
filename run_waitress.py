# -*- coding: utf-8 -*-
# run_waitress.py
# ⚡ Serveur backend Inventaire SaaS avec Waitress

import os
from waitress import serve
from app import app

if __name__ == "__main__":
    print("⚡ Serveur Inventaire SaaS démarrage en cours…")
    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
