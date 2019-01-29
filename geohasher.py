#!/usr/bin/env python3
"""A xkcd Geohashing script built for fun and profit."""
import datetime
import hashlib

import requests

TIME = str(datetime.datetime.now()).encode()

def main():
    get_ip()
    coords = geo_url_data()
    geohash(coords['latitude'], coords['longitude'], TIME)


def geohash(latitude, longitude, datedow):
    '''Compute geohash() using the Munroe algorithm.

    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543

    '''
    # https://xkcd.com/426/
    h = hashlib.md5(datedow).hexdigest()
    p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
    print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))


def get_ip():
    ip_url = 'https://api.ipify.org'
    ip = requests.get(ip_url)
    # print(ip.text)
    return ip.text


def geo_url_data():
    coords = {}
    geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + get_ip() + '.json'
    geo_data = requests.get(geo_request_url).json()
    # print(geo_data)
    coords['latitude'] = float(geo_data['latitude'])
    coords['longitude'] = float(geo_data['longitude'])
    print(coords)
    return coords


def distance_to_target():
    """Get the distance from ip location to geohash location"""
    pass


if __name__ == '__main__':
    main()
