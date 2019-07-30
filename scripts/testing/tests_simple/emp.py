import requests


class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def get_schedule(self, month):
        url = f"https://website.com/{self.last}/{month}"
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return "Bad response!"
