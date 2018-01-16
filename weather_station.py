#!/usr/bin/env python3

from pprint import pprint
from datetime import timezone

import logging
import requests
import sqlite3
import datetime
import time
import pytz


def main():
    weather = api_call()
    cli_display(weather)
    datetime_helper(weather)


def api_call():
    """Calls the OpenWeather API. """
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Perth,au&units=metric&appid=48b362375868b94f43172bcb13390ffc'
    # TODO remove hardcoded APIkey, put in enviroment. replace this key.
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
    utcdt = weather['dt']  # returns epoch TODO return localtime of location
    condition = [item['main'] for item in weather['weather']]

    # converter = datetime_helper(utcdt)

    print()
    print(f'{location} Weather:')
    print(f'Current Temp: {temp} Degrees Celsius')
    print(f'Conditions: {condition[0]}')
    print(f'UTC Epoch: {utcdt}')
    # print(f'As At: {converter}')
    print(f'Local Time: {datetime_helper(weather)}')


def store_output(data):
    pass

def datetime_helper(timestamp):
    """Get UTC timestamp from API, convert it to local for storage."""
    utcdt = timestamp['dt']  # returns epoch integer
    fmt = '%H:%M %d/%m/%Y'  # how the new string will be presented.

    # convert api epoch to datetime string using time
    new = time.strftime(fmt, time.localtime(utcdt))
    # convert api epoch to datetime string using datetime.datetime
    # new_v2 = datetime.datetime.fromtimestamp(utcdt).strftime(fmt)

    datetime_object = datetime.datetime.strptime(new, fmt)

    local_tz = pytz.timezone('Australia/Perth')
    local_time = datetime_object.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_time
    # return local_tz.normalize(local_time)


if __name__ == '__main__':
    main()
