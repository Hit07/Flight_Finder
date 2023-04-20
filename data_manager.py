SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/cafbb76b207d123/flightDeals/prices"
SHEETY_ENDPOINT = "https://api.sheety.co/cafbb767c733f083a83e1e17b207d123/flightDeals/users"
HEADER = {"Authorization": "Bearer hkshddnw35wbsjw6",
          'Content-Type': 'application/json'
          }

import requests


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        r = requests.get(url=SHEETY_ENDPOINT, headers=HEADER)
        return r.json()['users']
