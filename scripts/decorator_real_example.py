import time
import urllib.request
import urllib.error

# decorator 

def sleep(timeout, retry=3):
    def _decorator(fn):
        def wrapper(*args, **kwargs):
            retries = 0 
            while retries < retry:
                try:
                    value = function(*args, **kwargs)
                    if value is None:
                        return
                except:
                    print(f"Sleeping for {timeout} seconds before retry")
                    time.sleep(timeout)
                    retries += 1

        return wrapper
    return _decorator

# uptime function with retry decorator

def uptime(url):
    try:
        connection = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # email sys admin & log
        print(f"HTTPError: {e.code} for {url}")
        raise urllib.error.HTTPError
    except urllib.error.URLError as e:
        # email sys admin & log
        print(f"URLError: {e.code} for {url}")
        raise urllib.error.URLError
    else:
        # site is up
        print(f"{url} is up")

if __name__ == '__main__':
    # url = 'http://www.google.com/'
    url = 'http://www.google.com/fail'
    uptime(url)