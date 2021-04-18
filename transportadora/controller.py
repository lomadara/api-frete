from flask import g, request, Response, jsonify
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource
from typing import List, Dict

from .service import TransportadoraService
from .model import Transportadora
from .schema import TransportadoraSchema, transportadoraOpcoesSchema


api = Namespace('Transportadora')

@api.route('/')
class TransportadoraResource(Resource):
    @responds(schema=TransportadoraSchema(many=True))
    def get(self) -> List[Transportadora]:
        return TransportadoraService.get_all()
    
    @accepts(schema=TransportadoraSchema, api=api)
    @responds(schema=TransportadoraSchema)
    def post(self) -> Transportadora:
        transportadora = request.json
        return TransportadoraService.create(transportadora)

@api.route('/opcoes_frete')
class TransportadoraResource(Resource):
    @accepts(schema=transportadoraOpcoesSchema, api=api)
    @responds(schema=TransportadoraSchema(many=True))
    def post(self):
        pacote = request.json
        return TransportadoraService.getOpcoesDeFrete(pacote)
    
@api.route('/<int:ID>')
class TransportadoraIdResource(Resource):
    @responds(schema=TransportadoraSchema())
    def get(self, ID: int) -> Transportadora:
        return TransportadoraService().get_by_id(ID)

    def delete(self, ID: int) -> Response:
        return TransportadoraService().delete_by_id(ID)
    
    @accepts(schema=TransportadoraSchema, api=api)
    @responds(schema=TransportadoraSchema())
    def put(self, ID: int) -> Transportadora:
        transportadora = request.json
        return TransportadoraService.update(ID, transportadora)