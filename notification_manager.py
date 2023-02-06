import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        pass

    def joinSMSString(self, price, fly_from_city, fly_from_code,
                      fly_to_code, fly_to_city, date_from):
        body = f"Low price alert! Only {price} to fly from {fly_from_code}-{fly_from_city} to {fly_to_code}-{fly_to_city}, from {date_from}"
        return body

    def getDataFromDict(self, flight):
        notificationManager = NotificationManager()
        cityTo = flight['cityTo']
        cityCodeTo = flight['cityCodeTo']
        cityFrom = flight['cityFrom']
        cityCodeFrom = flight['cityCodeFrom']
        price = flight['price']
        date_from = flight['date_from']

        messageBody = notificationManager.joinSMSString(
            price, cityFrom, cityCodeFrom, cityTo, cityCodeTo, date_from)
        return messageBody

    def SendSMS(self, messageText: str):
        try:
            token = os.getenv("TWILIO_AUTH_TOKEN")
            account_sid = "ACb36d95fa5cfa3cbbdec26df81bd2526e"
            auth_token = token
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"{messageText}",
                from_="+16088796253",
                to="+16475635190"
            )
        except:
            print("Failing sending the message")
