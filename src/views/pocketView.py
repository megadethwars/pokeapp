# /src/views/GiroView

from flask import Flask, request, json, Response, Blueprint, g,current_app
from marshmallow import ValidationError
import requests
import statistics
from ..shared import returnCodes
from flask_restx import Api,fields,Resource
from werkzeug.security import generate_password_hash, check_password_hash
from ..services.pokeService import ServiceApi

app = Flask(__name__)
poke_api = Blueprint("users_api", __name__)

api = Api(poke_api)


nsPocket = api.namespace("users", description="API operations for usuarios")



def createUsers(req_data, listaObjetosCreados, listaErrores):
    #app.logger.info("Creando catalogo" + json.dumps(req_data))
    data = None
    
    return returnCodes.custom_response({"status":200}, 201, "TPM-1")



@nsPocket.route("")
class UsersList(Resource):
    @nsPocket.doc("lista de  usuarios")
    def get(self):

        serviceapi = ServiceApi()
        return serviceapi.processApi()

        url = current_app.config["POKE_URL"]
        print(url)

        #extraer berries names
        response = requests.get(url+"/"+"berry")
        data = response.json()


        berries = data['results']
        berries_names = [berry['name'] for berry in berries]

        detailed_data = []
        for berry in berries:
            berry_url = berry['url']
            berry_response = requests.get(berry_url)
            berry_data = berry_response.json()
            detailed_data.append(berry_data)


        growth_times = [int(berry['growth_time']) for berry in detailed_data]


        frequency_growth_time = {}

        for time in growth_times:
            if time in frequency_growth_time:
                frequency_growth_time[time] += 1
            else:
                frequency_growth_time[time] = 1

        frequency_growth_time_json = json.dumps(frequency_growth_time)

        response_data = {
            "berries_names": berries_names,
            "min_growth_time": min(growth_times),
            "median_growth_time": float(format(float(statistics.median(growth_times)), ".0f")),
            "max_growth_time": max(growth_times),
            "variance_growth_time": statistics.variance(growth_times),
            "mean_growth_time": statistics.mean(growth_times),
            "frequency_growth_time": frequency_growth_time
        }
        return returnCodes.custom_response(response_data, 201, "APP-1")

    @nsPocket.doc("Crear usuario")
    @nsPocket.response(201, "created")
    def post(self):
        return returnCodes.custom_response({"status":200}, 201, "APP-1")

    @nsPocket.doc("actualizar usuario")

    def put(self):
        return returnCodes.custom_response({"status":200}, 201, "APP-1")

