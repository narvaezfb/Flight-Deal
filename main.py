from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


FLY_FROM_CODE_DEFAULT = "YYZ"
DATE_FROM_DEFAULT = "01/02/2023"
DATE_TO_DEFAULT = "01/08/2023"
MAX_STOPOVERS = 0


def hasACheaperPrice(googleSheetFlight, responseLowestFlightPrice):
    return float(responseLowestFlightPrice) < float(googleSheetFlight)


def getTheMostCheapFlightFromApiResponse(listOfFlights):
    cheapestFlight = listOfFlights[0]
    lowest_price = cheapestFlight['price']

    for flight in listOfFlights:
        if flight['price'] < lowest_price:
            cheapestFlight = flight
            lowest_price = flight['price']
    return cheapestFlight


def main():
    # Initiate a new DataManager Object and fetch Data from Google sheet.
    dataManager = DataManager()
    flightData = FlightData()
    flightSearch = FlightSearch()
    notificationManager = NotificationManager()

    googleSheetFlights = dataManager.retrieveDataFromGoogleSheet()

    # Go through Each flightnfrom Google sheet
    for googleSheetFlight in googleSheetFlights:

        flyToCode = googleSheetFlight['iataCode']
        try:
            flightsResponse = flightSearch.fetchDataFromFlightSearchApi(
                FLY_FROM_CODE_DEFAULT, flyToCode, DATE_FROM_DEFAULT, DATE_TO_DEFAULT)
            flightsFormattedData = flightData.structureFlightDataFromSearchFlightResponse(
                flightsResponse)
            if len(flightsFormattedData) <= 0:
                raise Exception("Not data found")
        except Exception as e:
            print(e)
        else:
            cheapestFlight = getTheMostCheapFlightFromApiResponse(
                flightsFormattedData)
            # Compare if the "lowestPrice" from API is lower than current price from Google sheet
            if hasACheaperPrice(googleSheetFlight['lowestPrice'], cheapestFlight['price']):
                # Send SMS to user
                messageBody = notificationManager.getDataFromDict(
                    cheapestFlight)
                notificationManager.SendSMS(messageBody)
                print("Message has been sent")
            else:
                print("No cheapest flight found")


main()
