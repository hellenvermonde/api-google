from flask import make_response, jsonify
from src import db
from src.models.documentos import Documentos
import src.integrations.google_drive as google_drive
import json

def get_all_documents():
    service_drive = google_drive.main()
    
    # Call the Drive v3 API
    results = (
        service_drive.files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    
    items_drive = results.get("files", [])
    
    if not items_drive:
        return jsonify({'error': 404, 'message': 'Itens não encontrados'}), 404
    
    documents = [{'id': item['id'], 'name': item['name']} for item in items_drive]
    # return json.dumps({"files": documents}, indent=2)
    return documents
    

def get_document(id_emp):
    documentos_base = Documentos.query.get(id_emp)
    if not documentos_base:
        return{'erro':404, 'message':'Documento não encontrado'}
    
    documentos_serializados = []
    for documento_index in documentos_base:
        documento_serializado = {
            'id_documento': documento_index.id_documento,
            'titulo': documento_index.titulo,
            'tamanho': documento_index.tamanho,
            'pasta': documento_index.pasta,
            'tipo': documento_index.tipo,
            'data': documento_index.data,
            'origem': documento_index.origem,
            # Adicionar outros atributos conforme necessário
        }
        documentos_serializados.append(documento_serializado)
    
    return documentos_serializados

def create_document():
    pass

def update_document():
    pass

def delete_document():
    pass
