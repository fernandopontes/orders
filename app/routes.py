from flask import Blueprint, request, jsonify
from . import create_app, db
from .models import Produto, Pedido

routes = Blueprint('routes', __name__)

@routes.route('/produtos', methods=['POST'])
def adicionar_produto():
    data = request.json
    produto = Produto(nome=data['nome'], preco=data['preco'])
    db.session.add(produto)
    db.session.commit()
    return jsonify({'id': produto.id, 'nome': produto.nome, 'preco': produto.preco}), 201

@routes.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.json
    pedido = Pedido(produto_id=data['produto_id'], quantidade=data['quantidade'])
    db.session.add(pedido)
    db.session.commit()
    return jsonify({'id': pedido.id, 'produto_id': pedido.produto_id, 'quantidade': pedido.quantidade}), 201

@routes.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{'id': p.id, 'produto': p.produto.nome, 'quantidade': p.quantidade} for p in pedidos])