#!/usr/bin/env python3
from time import time

from requests_futures.sessions import FuturesSession
import logging
import pathlib
import requests
from bs4 import BeautifulSoup
import os
from random import choice

logging.basicConfig(level=logging.INFO)

def main():
    check_folder_exists()

    try:
        folder = os.path.join(pathlib.Path.home(), 'code/test/RFC')
        os.chdir(folder)
        logging.info(f'changed dir to: {folder}')
        start = time()
        iterate_over_rfcs()
        end = time()
        logging.info(f'This took: {end - start} to run!')

    except OSError:
        raise

    finally:
        cur_dir = pathlib.Path(__file__).parent
        logging.info(f'changed dir to: {cur_dir}')

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
    """Iterate over all possible RFC numbers on the IEEE webpage and then
    write them individually to files with a separate folder."""
    session = FuturesSession(max_workers=10)

    for num in range(0000, 8500):
        url = f"https://www.rfc-editor.org/rfc/rfc{num}.txt"
        future = session.get(url, headers=random_header())
        resp = future.result()
        if resp.status_code == 200:
            text = resp.text
            create_files(num, text)
            print(f"RFC {num:04d} downloaded!")

        else:
            print(f"RFC {num:04d} DOES NOT EXIST")



def create_files(num, text):
    """Function that creates text files from the RFC website.

    :argument num: takes the RFC number as part of the filename
    :argument text: writes the response text from the webpage into the file.
    """
    filename = f'RFC-{num:04d}.txt'
    with open(filename, 'w') as fout:
        fout.write(text)

def check_exists():
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