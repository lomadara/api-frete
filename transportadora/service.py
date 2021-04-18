from .model import Transportadora
from .interface import TransportadoraInterface

from typing import List
from app import db
from flask_sqlalchemy import Pagination
from sqlalchemy import asc, desc
from datetime import datetime
from flask import jsonify

class TransportadoraService():
    @staticmethod
    def get_all() -> List[Transportadora]:
        return Transportadora.query.filter_by().all()
    
    @staticmethod
    def get_by_id(ID: int) -> Transportadora:
        return Transportadora.query.filter_by(ID=ID).first_or_404(description='não existem transportadoras com o id {}'.format(ID))
    
    @staticmethod
    def update(ID: int, transportadora: TransportadoraInterface) -> Transportadora:
        existing_transportadora = Transportadora.query.filter_by(ID=ID).first_or_404(description='não existem transportadoras com o id {}'.formatr(ID))
        existing_transportadora.update(transportadora)
        db.session.commit()
        return existing_transportadora
    
    @staticmethod
    def create(transportadora: TransportadoraInterface) -> Transportadora:
        existing_trasnportadora = Transportadora.query.filter_by(NOME=transportadora.get('nome')).first()
        
        if bool(existing_trasnportadora):
            resp = jsonify({'message': 'Já existe um cadastro para a transportadora com o id {} .'.format(existing_trasnportadora.ID), 'id': existing_trasnportadora.ID})
            resp.status_code = 400
            return resp
        
        new_transportadora = Transportadora(
            ALTURA_MAX = transportadora.get('altura_max'),
            ALTURA_MIN = transportadora.get('altura_min'),
            LARGURA_MAX = transportadora.get('largura_max'),
            LARGURA_MIN = transportadora.get('largura_min'),
            PRAZO_ENTREGA = transportadora.get('prazo_entrega'),
            NOME = transportadora.get('nome'),
            CONSTANTE_FRETE = transportadora.get('constante_frete')
        )
        
        db.session.add(new_transportadora)
        db.session.commit()
        return new_transportadora
    
    @staticmethod
    def delete_by_id(ID: int) -> List[str]:
        transportadora = Transportadora.query.filter_by(ID=ID).first_or_404(description='não existem transportadoras com o id {}'.format(ID))
        db.session.delete(transportadora)
        db.session.commit()
        return [ANIME_ID]
    
    
    @staticmethod
    def getOpcoesDeFrete(pacote):
        dimensao = pacote.get('dimensao')
        peso = pacote.get('peso')
        transportadoras = Transportadora.query.filter(Transportadora.ALTURA_MAX >= dimensao.get('altura'))
        transportadoras = transportadoras.filter(Transportadora.ALTURA_MIN <= dimensao.get('altura'))
        transportadoras = transportadoras.filter(Transportadora.LARGURA_MAX >= dimensao.get('largura'))
        transportadoras = transportadoras.filter(Transportadora.LARGURA_MIN <= dimensao.get('largura')).all()
        response = []
        for transportadora in transportadoras:
            response.append({"nome": transportadora.NOME, "valor_frete": (peso * transportadora.CONSTANTE_FRETE) / 10, "prazo_dias": transportadora.PRAZO_ENTREGA})
        return jsonify(response)
        
    
    