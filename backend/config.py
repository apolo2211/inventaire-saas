# -*- coding: utf-8 -*-
# Configuration globale du SaaS Inventaire

# Base de données
DB_URI = "postgresql://user:password@localhost:5432/inventaire_db"

# Clé secrète pour JWT
SECRET_KEY = "votre_cle_jwt_secrete"

# Cloud Storage (AWS S3 ou autre)
CLOUD_STORAGE = "nom_bucket_saas"

# Stripe / Paiement (optionnel)
STRIPE_API_KEY = "sk_test_votre_clef"

# Autres paramètres
DEBUG = True
