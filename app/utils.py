# -*- coding: utf-8 -*-
import qrcode
import io
from werkzeug.security import generate_password_hash, check_password_hash

# Générer QR code pour un produit
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Hashage mot de passe
def hash_password(password):
    return generate_password_hash(password)

# Vérification mot de passe
def verify_password(password, hash_pw):
    return check_password_hash(hash_pw, password)
