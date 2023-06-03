import imp
import random
from flask import Flask, current_app, render_template
from flask_cors import CORS
from .config import app_config
from dotenv import load_dotenv, find_dotenv
from .shared import returnCodes



from .views.pocketView import nsPocket


from flask_restx import Api, fields, Resource


def create_app(env_name):
    """
    Create app
    """
    # app initiliazation
    
    app = Flask(__name__)
    # cors
    cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    
    app.config.from_object(app_config[env_name])


    app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://forrerunner97:Asterisco97@inventarioavs1.database.windows.net/avsInventory'

    
   
    api = Api(app,title="Poke API", version="1.1", description="A simple inventory API",)



    api.add_namespace(ns=nsPocket,path="/api/v1/pocket")

    @app.errorhandler(404) 
    def not_found(e):
        return returnCodes.custom_response(None, 404, 4041, "TPM-4")

    @app.errorhandler(400)
    def not_found(e):
        return returnCodes.custom_response(None, 400, 4001, "TPM-2")

    #@api.route('/home')
    #class HelloWorld(Resource):
    #    def get(self):
    #        return {'hello': 'world'}


    return app