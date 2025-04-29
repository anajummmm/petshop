from flask import Flask, jsonify, request
from models.produtos import products
from config.jwt_config import token_required

app = Flask(__name__)

@app.route('/products')
def listar_produtos():
    preco_asc = request.args.get('preco_asc')
    preco_desc = request.args.get('preco_desc')
    desc_part = request.args.get('description_part')

    lista = products.copy()

    if preco_asc:
        lista.sort(key=lambda x: x['product_price'])
    elif preco_desc:
        lista.sort(key=lambda x: x['product_price'], reverse=True)
    elif desc_part:
        lista = [p for p in lista if desc_part.lower() in p['product_description'].lower()]

    return jsonify(lista)

@app.route('/products/<int:id>')
def get_produto(id):
    for produto in products:
        if produto["id"] == id:
            return jsonify(produto)
    return jsonify({'message': 'produto nao encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
