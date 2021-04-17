from app import db


class Transportadora(db.Model):
    ID: int = db.Column(db.Integer, primary_key=True, nullable=True)
    ALTURA_MAX: int = db.Column(db.Integer, primary_key=True)
    ALTURA_MIN: int = db.Column(db.Integer)
    LARGURA_MAX: int = db.Column(db.Integer)
    LARGURA_MIN: int = db.Column(db.Integer)
    PRAZO_ENTREGA: int = db.Column(db.Integer)
    NOME: str = db.Column(db.String(200))
    CONSTANTE_FRETE: float = db.Column(db.Float)
    
    def update(self, ALTURA_MAX: int, ALTURA_MIN: int, LARGURA_MAX: int, LARGURA_MIN: int, PRAZO_ENTREGA: int, NOME: str, CONSTANTE_FRETE: float):
        self.ALTURA_MAX = ALTURA_MAX
        self.ALTURA_MIN = ALTURA_MIN
        self.LARGURA_MAX = LARGURA_MAX
        self.LARGURA_MIN = LARGURA_MIN
        self.PRAZO_ENTREGA = PRAZO_ENTREGA
        self.NOME = NOME
        self.CONSTANTE_FRETE = CONSTANTE_FRETE