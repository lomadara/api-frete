# cadastro de transportadoras [POST]
http://localhost:8080/v1/transportadora

{
    "ALTURA_MAX": 140,
    "ALTURA_MIN": 5,
    "LARGURA_MAX": 125,
    "LARGURA_MIN": 13,
    "PRAZO_ENTREGA": 4,
    "NOME": "Entrega KaBuM",
    "CONSTANTE_FRETE": 0.2
}

# listagem de transportadoras [GET]
http://localhost:8080/v1/transportadora

# get por id de transportadoras [GET]
http://localhost:8080/v1/transportadora/1

# deleção de transportadora [DELETE]
http://localhost:8080/v1/transportadora/1

# update de transportadora [PUT]
http://localhost:8080/v1/transportadora/1

{
    "ALTURA_MAX": 140,
    "ALTURA_MIN": 5,
    "LARGURA_MAX": 125,
    "LARGURA_MIN": 13,
    "PRAZO_ENTREGA": 4,
    "NOME": "Entrega KaBuM",
    "CONSTANTE_FRETE": 0.2
}

# opções de frete [PUT]
http://localhost:8080/v1/transportadora/opcoes_frete

{
	"dimensao": {"altura":102, "largura":40},
	"peso":400
}
```
