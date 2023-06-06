from ..shared import returnCodes
from flask import Flask, json, Response, Blueprint, g,current_app
import requests
import statistics
import matplotlib.pyplot as plt
import base64
import io
from ..models.BerryStats import BerryModel
class ServiceApi():



    """
        Methodo encargado de generar estadisticas de berrys, consulta cada url de estas y toma el growth_time para realizar
        las estadisticas, adicionalmente se genera el histograma de matplotlib y se envia como base64
    """

    def processApiHist(self):
        try:
            url = current_app.config["POKE_URL"]

            response = requests.get(url+"/"+"berry")

            if response.status_code!=200:

                return returnCodes.custom_response({}, response.status_code, "APP-11",str(response.text))

            data = response.json()
            berries = data['results']

            detailed_data = []
            for berry in berries:
                berry_url = berry['url']
                berry_response = requests.get(berry_url)
                berry_data = berry_response.json()
                detailed_data.append(berry_data)


            growth_times = [int(berry['growth_time']) for berry in detailed_data]

            berry_model = BerryModel([], growth_times)

            labels1 = ['Min Growth Time', 'Max Growth Time', 'Mean Growth Time', 'Median Growth Time', 'Variance Growth Time']
            values1 = [berry_model.min_growth_time, berry_model.max_growth_time, berry_model.mean_growth_time, float(format(float(berry_model.median_growth_time), ".0f")), round(berry_model.variance_growth_time,2)]

            labels2 = list(berry_model.frequency_growth_time.keys())
            values2 = list(berry_model.frequency_growth_time.values())

            fig, axs = plt.subplots(1, 2, figsize=(10, 5))

            # Histograma 1
            axs[0].bar(labels1, values1)
            axs[0].set_title('growth_time berrys')
            axs[0].set_xlabel('Variables')
            axs[0].set_ylabel('Valores')
            axs[0].set_xticklabels(labels1, rotation=45, ha='right')

            # Histograma 2
            axs[1].bar(labels2, values2)
            axs[1].set_title('frequency_growth_time')
            axs[1].set_xlabel('growth_time')
            axs[1].set_ylabel('frequency')

            plt.tight_layout()
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)

            #a formato base64
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            image_str = str(image_base64)


            return returnCodes.custom_response({"image":image_str}, 200, "APP-3")
        except Exception as ex:
            return returnCodes.custom_response({}, 500, "APP-7",str(ex))


    """
        Methodo encargado de generar estadisticas de berrys, consulta cada url de estas y toma el growth_time para realizar
        las estadisticas y generarlas en el response
    """
    def processApi(self):

        try:
            url = current_app.config["POKE_URL"]

            response = requests.get(url+"/"+"berry")

            if response.status_code!=200:

                return returnCodes.custom_response({}, response.status_code, "APP-11",str(response.text))

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


            berry_model = BerryModel(berries_names, growth_times)

            response_data = {
                "berries_names": berries_names,
                "min_growth_time":  berry_model.min_growth_time,
                "median_growth_time": float(format(float(berry_model.median_growth_time), ".0f")),
                "max_growth_time": berry_model.max_growth_time,
                "variance_growth_time": round(berry_model.variance_growth_time,2),
                "mean_growth_time": berry_model.mean_growth_time,
                "frequency_growth_time": berry_model.frequency_growth_time
            }


            return returnCodes.custom_response(response_data, 200, "APP-3")
        except Exception as ex:
            return returnCodes.custom_response({}, 500, "APP-7",str(ex))