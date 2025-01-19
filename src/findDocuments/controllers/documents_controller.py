from flask import jsonify # type: ignore
from src.findDocuments.services.documents_service import get_all_documents, get_document

def get_infos_all_documents():
    documentos = get_all_documents()

    return documentos

def get_infos_one_document(data):
    nome_doc = data['nome_documento']
    documento = get_document(nome_doc)
    return documento

