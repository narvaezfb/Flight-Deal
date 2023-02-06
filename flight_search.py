import requests
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()


class FlightSearch:
    flight_search_url_endpoint = "https://api.tequila.kiwi.com/v2/search"
    API_KEY = os.getenv("FLIGHT_SEARCH_API")

    def __init__(self) -> None:
        pass

    def fetchDataFromFlightSearchApi(self, fly_from: str, fly_to: str, date_from: str, date_to: str):
        try:
            flight_search_headers = {
                "apikey": self.API_KEY,
            }
            flight_search_params = {
                "fly_from": fly_from,
                "fly_to": fly_to,
                "date_from": date_from,
                "date_to": date_to
            }
            response = requests.get(url=self.flight_search_url_endpoint,
                                    params=flight_search_params, headers=flight_search_headers)
        except:
            response.raise_for_status()
        else:
            return response.json()
