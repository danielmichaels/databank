#!/usr/bin/env python3

from pprint import pprint
from datetime import datetime

import logging
import requests


def main():
    weather = api_call()
    cli_display(weather)


def api_call():
    """Calls the OpenWeather API. """
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Perth,au&units=metric&appid=48b362375868b94f43172bcb13390ffc'
    # TODO remove hardcoded APIkey, put in enviroment.
    resp = requests.get(url)
    if resp.status_code != 200:
        print('error somewhere')
    weather = resp.json()
    pprint(weather)
    # pprint(weather['main']['temp'])
    return weather


def cli_display(weather):
    """Simple cli print out of the wanted API data.

    :arg: takes in JSON data from api_call function.
    """
    location = weather['name']
    temp = weather['main']['temp']
    utcdt = weather['dt'] # returns epoch TODO return localtime of location
    condition = [item['main'] for item in weather['weather']]

    print()
    print(f'{location} Weather:')
    print(f'Current Temp: {temp} Degrees Celsius')
    print(f'Conditions: {condition[0]}')
    print(f'As At: {utcdt}')


if __name__ == '__main__':
    main()
