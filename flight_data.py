from flight_search import FlightSearch


class FlightData:

    def __init__(self) -> None:
        pass

    def structureFlightDataFromSearchFlightResponse(self, response):
        try:
            listOfFlights = []
            listOfFlightsFromResponse = response['data']

            for flight in listOfFlightsFromResponse:
                cityTo = flight['cityTo']
                cityCodeTo = flight['cityCodeTo']
                cityFrom = flight['cityFrom']
                cityCodeFrom = flight['cityCodeFrom']
                price = flight['price']
                date_from = flight['local_departure']

                flightFormatted = {"cityTo": cityTo,
                                   "cityCodeTo": cityCodeTo,
                                   "cityFrom": cityFrom,
                                   "cityCodeFrom": cityCodeFrom,
                                   "price": price,
                                   "date_from": date_from
                                   }
                listOfFlights.append(flightFormatted)
        except:
            print("something went wrong by formatting data")
        else:
            return listOfFlights
