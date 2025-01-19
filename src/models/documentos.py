from src import db



class Documentos(db.Model):
    __tablename__ = 'documentos'
    
    id_documento = db.Column(db.String(10), primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    tamanho = db.Column(db.Numeric(precision=15, scale=2), nullable=False)
    pasta = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=True)
    origem = db.Column(db.String, nullable=True)

    def serialize(self):
        return {
            'id_documento': self.id_documento,
            'titulo': self.titulo,
            'tamanho': self.tamanho,
            'pasta': self.pasta,
            'tipo': self.tipo,
            'data': self.data,
            'origem': self.origem,
            # Incluir todos os outros atributos que você deseja serializar
        }