from ..shared import returnCodes
from flask import Flask, request, json, Response, Blueprint, g,current_app
import requests
import statistics


class ServiceApi():

    def processApi(self):
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