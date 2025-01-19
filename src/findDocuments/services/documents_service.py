from src import db
from src.models.documentos import Documentos

def get_all_documents():
    docuemntos_base = Documentos.query.all()
    
    if not docuemntos_base:
        return{'erro':404, 'message':'Documentos não encontrados'}
    
    documentos_serializados = []
    for documento_index in docuemntos_base:
        documento_serializado = {
            'id_emp': documento_index.id_emp,
            'bairro': documento_index.bairro,
            'cartorio': documento_index.cartorio,
            # Adicionar outros atributos conforme necessário
        }
        documentos_serializados.append(documento_serializado)
    
    return documentos_serializados

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
