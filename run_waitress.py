from waitress import serve
from app import app

print("⚡ Serveur démarrage en cours…")

serve(app, host="127.0.0.1", port=5500)


print("✅ Serveur lancé sur http://127.0.0.1:5000")
