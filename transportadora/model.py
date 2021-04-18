from app import db
from .interface import TransportadoraInterface

class Transportadora(db.Model):
    ID: int = db.Column(db.Integer, primary_key=True, nullable=True)
    ALTURA_MAX: int = db.Column(db.Integer, primary_key=True)
    ALTURA_MIN: int = db.Column(db.Integer)
    LARGURA_MAX: int = db.Column(db.Integer)
    LARGURA_MIN: int = db.Column(db.Integer)
    PRAZO_ENTREGA: int = db.Column(db.Integer)
    NOME: str = db.Column(db.String(200))
    CONSTANTE_FRETE: float = db.Column(db.Float)
    
    def update(self, transportadora: TransportadoraInterface):
        self.ALTURA_MAX = transportadora.get('altura_max')
        self.ALTURA_MIN = transportadora.get('altura_min')
        self.LARGURA_MAX = transportadora.get('largura_max')
        self.LARGURA_MIN = transportadora.get('largura_min')
        self.PRAZO_ENTREGA = transportadora.get('prazo_entrega')
        self.NOME = transportadora.get('nome')
        self.CONSTANTE_FRETE = transportadora.get('constante_frete')