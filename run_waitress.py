# -*- coding: utf-8 -*-
# run_waitress.py
# ⚡ Serveur backend Inventaire SaaS avec Waitress

from waitress import serve
from app import app
import os

port = int(os.environ.get("PORT", 5000))

serve(app, host="0.0.0.0", port=port)
