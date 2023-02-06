import requests


class DataManager:
    # ENDPOINT
    google_datasheet_endpoint = "https://api.sheety.co/7269c1cedc011e77d60fe35eb9da9a1b/flightDeals/prices"

    def __init__(self) -> None:
        pass

    def retrieveDataFromGoogleSheet(self):
        try:
            response = requests.get(url=self.google_datasheet_endpoint)
        except:
            response.raise_for_status()
        else:
            data = response.json()
            prices = data['prices']
            return prices
