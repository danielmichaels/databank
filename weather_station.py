#!/usr/bin/env python3

from pprint import pprint

import contextlib
import datetime
import pytz
import requests
import sqlite3

API_KEY = os.environ.get(OPENWEATHERAPI) 

def main():
    weather = api_call()
    cli_display(weather)
    timestamp = datetime_helper(weather)
    create_db()
    insert_data(weather, timestamp)
    recent_weather = get_data()
    pprint(recent_weather)


def api_call():
    """Calls the OpenWeather API. """
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Perth,au&units=metric&appid=' + API_KEY
    resp = requests.get(url)
    if resp.status_code != 200:
        print('error somewhere')
    weather = resp.json()
    pprint(weather)
    return weather


def cli_display(weather):
    """Simple cli print out of the wanted API data.

    :arg: takes in JSON data from api_call function.
    """
    location = weather['name']
    temp = weather['main']['temp']
    utcdt = weather['dt']  # returns epoch
    condition = [item['main'] for item in weather['weather']]

    print()
    print('{location} Weather:'.format(location=location))
    print('Current Temp: {temp} Degrees Celsius'.format(temp=temp))
    print('Conditions: {condition[0]}'.format(condition=condition))
    print('UTC Epoch: {utcdt}'.format(utcdt=utcdt))
    print('Local Time: {}'.format(datetime_helper(weather)))


def datetime_helper(weather_json):
    """Get UTC timestamp from API, convert it to local for storage."""
    utcdt = weather_json['dt']  # returns epoch integer
    # convert api epoch to datetime string using datetime.datetime
    new = datetime.datetime.fromtimestamp(utcdt).strftime('%H:%M %d/%m/%Y')
    datetime_object = datetime.datetime.strptime(new, '%H:%M %d/%m/%Y')

    local_tz = pytz.timezone('Australia/Perth')
    local_time = datetime_object.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_time


def create_db():
    """Create the database."""
    try:
        conn = sqlite3.connect('weather_test1.db')
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS weather("
            "location TEXT, temp TEXT, conditons TEXT, "
            "utc_epoch INTEGER PRIMARY KEY, local TEXT)")
    finally:
        if conn:
            conn.close()


def insert_data(api_call, timestamp):
    """Insert each api call into database."""
    location = api_call['name']
    temp = api_call['main']['temp']
    utcdt = api_call['dt']
    condition = [item['main'] for item in api_call['weather']]

    with contextlib.closing(sqlite3.connect('weather_test1.db')) as cursor:
        # cursor.execute("INSERT INTO weather VALUES ("
        cursor.execute("INSERT OR IGNORE INTO weather VALUES ("
                       ":location, :temp, :conditions, :utc_epoch, :local)",
                       {'location': location, 'temp': temp,
                        'conditions': condition[0],
                        'utc_epoch': utcdt, 'local': timestamp})
        cursor.commit()


def get_data():
    """Read the data in the database."""
    # TODO get epoch and now make local.
    with contextlib.closing(sqlite3.connect('weather_test1.db')) as cursor:
        data = cursor.execute("SELECT * FROM weather")
        return data.fetchall()


def join_tables():
    """Practice a join here."""
    pass


if __name__ == '__main__':
    main()
