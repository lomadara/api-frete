from typing import List, Dict
from mypy_extensions import TypedDict


class TransportadoraInterface(TypedDict, total=False):
    altura_max: int
    altura_min: int
    largura_max: int
    largura_min: int
    prazo_entrega: int
    nome: str
    constante_frete: float