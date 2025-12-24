# -*- coding: utf-8 -*-
# Script test pour générer un QR code produit

from app.utils import generate_qr_code

if __name__ == "__main__":
    code = input("Entrez le code unique du produit: ")
    qr_image = generate_qr_code(code)
    with open(f"{code}.png", "wb") as f:
        f.write(qr_image.getbuffer())
    print(f"QR code généré: {code}.png")
