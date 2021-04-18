from marshmallow import fields, Schema, EXCLUDE


class TransportadoraSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    id = fields.Integer(attribute='ID', required=False)
    altura_max = fields.Integer(attribute='ALTURA_MAX', required=True)
    altura_min = fields.Integer(attribute='ALTURA_MIN', required=True)
    largura_max = fields.Integer(attribute='LARGURA_MAX', required=True)
    largura_min = fields.Integer(attribute='LARGURA_MIN', required=True)
    prazo_entrega = fields.Integer(attribute='PRAZO_ENTREGA', required=True)
    nome = fields.String(attribute='NOME', required=True)
    constante_frete = fields.Float(attribute='CONSTANTE_FRETE', required=True)
    
class DimensaoSchema(Schema):
    altura = fields.Integer(required=True)
    largura = fields.Integer(required=True)
    
class transportadoraOpcoesSchema(Schema):
    dimensao = fields.Nested(DimensaoSchema, required=True)
    peso = fields.Integer(required=True)