#!/usr/bin/env python3
"""A xkcd Geohashing script built for fun and profit."""
import hashlib
# from antigravity import geohash

import requests


def main():
    get_ip()
    geo_url_data()


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
    print(ip.text)
    return ip.text


def geo_url_data():
    pass


if __name__ == '__main__':
    main()
