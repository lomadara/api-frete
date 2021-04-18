# criação do banco de dados [MYSQL]
CREATE DATABASE `teste_kabum` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

# criação das tabelas
CREATE TABLE `transportadora` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ALTURA_MAX` int(11) NOT NULL,
  `ALTURA_MIN` int(11) NOT NULL,
  `LARGURA_MAX` int(11) NOT NULL,
  `LARGURA_MIN` int(11) NOT NULL,
  `PRAZO_ENTREGA` int(11) NOT NULL,
  `NOME` varchar(200) NOT NULL,
  `CONSTANTE_FRETE` float NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

# massa inicial de dados
SET NAMES utf8 ;
DROP TABLE IF EXISTS `transportadora`;
SET character_set_client = utf8mb4 ;
CREATE TABLE `transportadora` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ALTURA_MAX` int(11) NOT NULL,
  `ALTURA_MIN` int(11) NOT NULL,
  `LARGURA_MAX` int(11) NOT NULL,
  `LARGURA_MIN` int(11) NOT NULL,
  `PRAZO_ENTREGA` int(11) NOT NULL,
  `NOME` varchar(200) NOT NULL,
  `CONSTANTE_FRETE` float NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `transportadora` WRITE;
INSERT INTO `transportadora` VALUES (1,200,10,140,6,6,'Entrega Ninja',0.3),(2,140,5,125,13,4,'Entrega KaBuM',0.2);
UNLOCK TABLES;

# a configuração da url da base fica no arquivo .env
SQLALCHEMY_DATABASE_URI="mysql://usuario:senha@host:porta/base"

# instalação de dependencias
pipenv install

# depois execute
pipenv shell

# execução do projeto
python main.py

# cadastro de transportadoras [POST]
http://localhost:8080/v1/transportadora

{
    "altura_max": 140,
    "altura_min": 5,
    "largura_max": 125,
    "largura_min": 13,
    "prazo_entrega": 4,
    "nome": "Entrega KaBuM",
    "constante_frete": 0.2
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
    "id": 2,
    "altura_max": 140,
    "altura_min": 5,
    "largura_max": 125,
    "largura_min": 13,
    "prazo_entrega": 4,
    "nome": "Entrega KaBuM",
    "constante_frete": 0.2
}

# opções de frete [PUT]
http://localhost:8080/v1/transportadora/opcoes_frete

{
    "dimensao": {"altura":102, "largura":40},
    "peso":400
}
```
