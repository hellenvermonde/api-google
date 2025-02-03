from flask import Blueprint, jsonify, request # type: ignore
from ..findDocuments.controllers import documents_controller


documents_bp = Blueprint('documentos', __name__)

@documents_bp.route('/listAll', methods=['POST', 'GET'])
def get_documents():
    responde = documents_controller.get_infos_all_documents()
    return jsonify(responde)

@documents_bp.route('/post', methods=['POST','GET'])
def post_document():
    data = request.get_json()
    response = documents_controller.get_infos_one_document(data)
    return jsonify(response)