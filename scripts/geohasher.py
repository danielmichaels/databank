#!/usr/bin/env python3
"""A xkcd Geohashing script built for fun and profit."""
import datetime
import hashlib

import requests
import webbrowser
from geopy import distance

TIME = str(datetime.datetime.now()).encode()


def main():
    get_ip()
    start = geo_url_data()
    end = geohash(start["latitude"], start["longitude"], TIME)
    distance_to_target(start, end)


def geohash(latitude, longitude, datedow):
    """Compute geohash() using the Munroe algorithm.

    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543

    """
    # https://xkcd.com/426/
    end_coords = {}
    h = hashlib.md5(datedow).hexdigest()
    p, q = [("%f" % float.fromhex("0." + x)) for x in (h[:16], h[16:32])]
    # print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))
    end_coords["latitude"] = latitude + float(p[1:])
    end_coords["longitude"] = longitude + float(q[1:])
    return end_coords


def get_ip():
    ip_url = "https://api.ipify.org"
    ip = requests.get(ip_url)
    return ip.text


def geo_url_data():
    coords = {}
    geo_request_url = "https://get.geojs.io/v1/ip/geo/" + get_ip() + ".json"
    geo_data = requests.get(geo_request_url).json()
    coords["latitude"] = float(geo_data["latitude"])
    coords["longitude"] = float(geo_data["longitude"])
    return coords


def distance_to_target(start, end):
    """Get the distance from ip location to geohash location"""
    start = start["latitude"], start["longitude"]
    end = end["latitude"], end["longitude"]
    print(f"start: {start}, end: {end}")
    distance_away = distance.distance(start, end).km
    print(f"Distance from start point is {distance_away:.2f} kilometers away.")
    launch_page(end)


def launch_page(endpoint):
    """Launch googlemaps with lat long of endpoint."""
    base_url = "https://www.google.com/maps/search/?api=1&query={},{}&zoom=12"
    url = base_url.format(endpoint[0], endpoint[1])
    webbrowser.open(url)


if __name__ == "__main__":
    main()
