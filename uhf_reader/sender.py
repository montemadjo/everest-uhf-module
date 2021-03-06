import requests


class Sender:
    def __init__(self, URL):
        self.url = URL

    def postStadionUhfCards(self, data) -> None:
        response = requests.post(self.url, json=data, timeout=4)
        if response == "ok":
            print("Data posted to cloud")
