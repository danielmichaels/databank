"""User agent randomiser."""
import random
import requests


def main():
    ua = check_ua()
    print(ua)


def user_agent():
    """From a list of user agents randomly select one."""
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    ]
    agent = random.choice(user_agents)

    return agent


def check_ua():
    """
    Given a URL return the response with a random header.
    
    The URL will return our header information as a JSON object. We parse it
    to retrieve only the user agent data.
    """
    url = "https://www.whatsmyua.info/api/v1/ua?="
    resp = requests.get(url, headers={"User-Agent": user_agent()})
    ua = resp.json()[0]["ua"]["rawUa"]
    return ua


if __name__ == "__main__":
    main()
