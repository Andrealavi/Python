# Assignment: Create a script which takes a province's name from the user, takes the coordinates from ./data/provinces.json file
# and then uses Open Meteo API to get te actual and the apparent temperatura of that province.
# The script has to manage the case in which the province is not in ./data/provinces.json

import requests
import datetime
import json

hours = int(datetime.datetime.now().strftime("%H"))

with open('./data/provinces.json', 'r') as f:
    provinces = json.load(f)
    nomiProvinces = [province for province in provinces]


def getTemperature():
    try:
        province = input(
            'Insert the name of the province you want to get temperatura: ').capitalize()

        if province not in nomiProvinces:
            raise Exception('Province not found, try again')

        lat = provinces[province]['lat']
        lon = provinces[province]['lon']

        url = 'https://api.open-meteo.com/v1/forecast?&hourly=temperature_2m,apparent_temperature&timezone=Europe/Rome&latitude={}&longitude={}'.format(
            lat, lon)

        request = requests.get(url).json()['hourly']

        print('Actual Temperature in {} at {} '.format(province, hours),
              request['temperature_2m'][hours - 1], "°C")
        print('Apparent Temperature in {} at {} '.format(province, hours),
              request['apparent_temperature'][hours - 1], "°C")
    except Exception as error:
        print(error, "\n")
        getTemperature()


getTemperature()
