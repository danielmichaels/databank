#!/usr/bin/env python3
from time import time

import logging
import pathlib
import requests
from bs4 import BeautifulSoup
import os
from random import choice

logging.basicConfig(level=logging.INFO)

def main():
    # iterate_over_rfcs()
    create_files()
    check_folder_exists()

def random_header():
    desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
    return {'User-Agent': choice(desktop_agents), 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def iterate_over_rfcs():
    for num in range(0000,1000):
        url = f"https://www.rfc-editor.org/rfc/rfc{num}.txt"
        resp = requests.get(url, headers=random_header())
        if resp.status_code == 200:
            print(f"RFC {num:04d} exists")
        else:
            print(f"RFC {num:04d} DOES NOT EXIST")



def create_files():
    pass

def check_exits():
    pass


def check_folder_exists():
    """Create the folder that stores all the RFC files if it does not exist."""
    folder = os.path.join(pathlib.Path.home(), 'code/test/RFC')
    try:
        if not os.path.exists(folder):
            logging.info('Folder doesn\'t exist...')
            os.makedirs(folder)
            logging.info(f'Folder: {folder} created!')
        else:
            logging.info(f'{folder} already exists.')
    except OSError:
        raise

if __name__ == '__main__':
    main()