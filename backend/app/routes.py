# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required
from app.models import db, Product, Movement
from app.utils import generate_qr_code
from app.documents import generate_word, generate_excel, generate_pdf

routes_bp = Blueprint('routes', __name__)

# Ajouter un produit
@routes_bp.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    product = Product(
        name=data.get('name'),
        description=data.get('description'),
        quantity=data.get('quantity',0),
        value=data.get('value',0.0),
        code_unique=data.get('code_unique')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"msg": "Produit ajouté"}), 201

# Lister tous les produits
@routes_bp.route('/products', methods=['GET'])
@jwt_required()
def list_products():
    products = Product.query.all()
    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "quantity": p.quantity,
            "value": p.value,
            "code_unique": p.code_unique
        })
    return jsonify(result), 200

# Export Word
@routes_bp.route('/reports/word/<int:product_id>', methods=['GET'])
@jwt_required()
def export_word(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"msg": "Produit non trouvé"}), 404
    file_stream = generate_word({
        "name": product.name,
        "description": product.description,
        "quantity": product.quantity,
        "code_unique": product.code_unique
    })
    return send_file(file_stream, as_attachment=True, download_name=f"{product.name}.docx")

# Export Excel
@routes_bp.route('/reports/excel', methods=['GET'])
@jwt_required()
def export_excel():
    products = Product.query.all()
    data = [{"name":p.name,"description":p.description,"quantity":p.quantity,"value":p.value,"code_unique":p.code_unique} for p in products]
    file_stream = generate_excel(data)
    return send_file(file_stream, as_attachment=True, download_name="inventaire.xlsx")

# Export PDF
@routes_bp.route('/reports/pdf', methods=['GET'])
@jwt_required()
def export_pdf_route():
    products = Product.query.all()
    data = [{"name":p.name,"quantity":p.quantity,"value":p.value} for p in products]
    file_stream = generate_pdf(data)
    return send_file(file_stream, as_attachment=True, download_name="rapport.pdf")

