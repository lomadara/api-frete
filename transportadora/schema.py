from marshmallow import fields, Schema, EXCLUDE

class PaginationSchema(Schema):
    page = fields.Integer(attribute='page')
    pages = fields.Integer(attribute='pages')


class TransportadoraSchema(Schema):
    class Meta:
        unknown = EXCLUDE
    
    ID = fields.Integer(attribute='ID', required=True)
    ALTURA_MAX = fields.Integer(attribute='ALTURA_MAX', required=True)
    ALTURA_MIN = fields.Integer(attribute='ALTURA_MIN', required=True)
    LARGURA_MAX = fields.Integer(attribute='LARGURA_MAX', required=True)
    LARGURA_MIN = fields.Integer(attribute='LARGURA_MIN', required=True)
    PRAZO_ENTREGA = fields.Integer(attribute='PRAZO_ENTREGA', required=True)
    NOME = fields.String(attribute='NOME', required=True)
    CONSTANTE_FRETE = fields.Float(attribute='CONSTANTE_FRETE', required=True)


class TransportadoraPageSchema(PaginationSchema):
    items = fields.List(fields.Nested(TransportadoraSchema), attribute='items')