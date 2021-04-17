from flask import Flask, Blueprint
from flask_restx import Api
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    app.config.from_object('app.config.Config')

    db.init_app(app)
    
    CORS(app, resources={r"/v1/*": {"origins": "*"}})
    
    with app.app_context():
        from transportadora.controller import api as transportadora_ns
        
        blueprint = Blueprint('api', __name__, url_prefix='/v1')
        api = Api(
            blueprint,
            title='teste api v1',
            version='1.0',
            description='teste restful api',
        )
        app.register_blueprint(blueprint)
        
        api.add_namespace(transportadora_ns, path='/transportadora')
        
        return app
        