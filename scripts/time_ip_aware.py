"""
Helper functions for doing datetime things with ip addresses.
"""


def external_ip():
    """Returns users external IP address."""
    retries = HTTPAdapter(max_retries=3)
    session = requests.Session()
    api = "https://api.ipify.org"
    session.mount(api, retries)
    try:
        resp = session.get(api)
        return resp.text
    except requests.ConnectionError as e:
        print(e)


def client_timezone():
    """
    Returns the localtime for the user making the query based off their IP address.
    """
    user_time = external_ip()
    url = f"https://ipgeolocation.com/{user_time}"
    try:
        ip_data = requests.get(url).json()
        timezone = ip_data["timezone"]
        return timezone
    except requests.ConnectionError:
        # fallback to plain datetime
        return datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y")
