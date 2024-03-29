# /src/views/pocketView

from flask import Flask, request, json, Response, Blueprint, g,current_app,render_template
from marshmallow import ValidationError
import requests
import statistics
from ..shared import returnCodes
from flask_restx import Api,fields,Resource
from werkzeug.security import generate_password_hash, check_password_hash
from ..services.pokeService import ServiceApi

app = Flask(__name__)
poke_api = Blueprint("poke_api", __name__)

api = Api(poke_api)


nsPocket = api.namespace("Poke", description="API operations for poke API")


@nsPocket.route("/allBerryStats")
class UsersList(Resource):
    @nsPocket.doc("endpoint para consumir estadisticas de berries y los nombres")
    @nsPocket.response(200, "Consulta exitosa")
    @nsPocket.response(500, "Ocurrio un error interno")
    @nsPocket.response(404, "Recurso no encontrado")
    @nsPocket.response(409, "Ocurrio un conflicto interno")
    def get(self):

        serviceapi = ServiceApi()
        return serviceapi.processApi()

@nsPocket.route("/allBerryStats/hist")
class UsersList(Resource):
    @nsPocket.doc("endpoint para consumir estadisticas, enviando el histograma como imagen")
    @nsPocket.response(200, "Consulta exitosa")
    @nsPocket.response(500, "Ocurrio un error interno")
    @nsPocket.response(404, "Recurso no encontrado")
    @nsPocket.response(409, "Ocurrio un conflicto interno")
    def get(self):

        serviceapi = ServiceApi()
        return serviceapi.processApiHist()





