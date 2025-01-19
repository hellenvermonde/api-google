from flask import Blueprint, jsonify, request # type: ignore
from src.tests import conexao_api

testes_bp = Blueprint('testes', __name__)

@testes_bp.route('/pin', methods=['POST', 'GET'])
def get_conexao_api_routes():
    response = conexao_api.get_teste_de_api()
    return jsonify(response)