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
    #cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    
    #app.config.from_object(app_config[env_name])


    #api = Api(app,title="Poke API", version="1.1", description="A simple poke API",)


    #api.add_namespace(ns=nsPocket,path="/api/v1/pocket")

    

    return app