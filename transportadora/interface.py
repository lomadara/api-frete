from typing import List, Dict
from mypy_extensions import TypedDict


class TransportadoraInterface(TypedDict, total=False):
    ALTURA_MAX: int
    ALTURA_MIN: int
    LARGURA_MAX: int
    LARGURA_MIN: int
    PRAZO_ENTREGA: int
    NOME: str
    CONSTANTE_FRETE: float