# Flight_Finder
Cheap Flight Finder is a web-based application that allows users to search for the cheapest flights from one destination to another. The application uses APIs provided by Tequila Kiwi, Sheety, and Oops Python to retrieve data from various airlines and display the results in a user-friendly manner.

# Getting Started
To use the Cheap Flight Finder application, you will need to have a Google Sheets account and a Twilio account. Follow the steps below to set up the project:
- Clone the repository to your local machine.
- Install the required dependencies by running pip install -r requirements.txt.
- Create a Google Sheet to keep track of the locations you want to visit and their lowest prices. The sheet should have the following columns:

       * Location: The name of the location you want to visit.
       * Price: The lowest price you are willing to pay for a round-trip flight to that location.
       
- Create a Twilio account and set up a phone number to receive SMS notifications.
- Create a .env file with the following environment variables:

       * SHEETY_ENDPOINT: The endpoint URL for your Google Sheet API.
       * KIWI_API_KEY: Your Tequila Kiwi API key.
       * TWILIO_ACCOUNT_SID: Your Twilio account SID.
       * TWILIO_AUTH_TOKEN: Your Twilio authentication token.
       * TWILIO_PHONE_NUMBER: The Twilio phone number to send SMS notifications from.
       * MY_PHONE_NUMBER: Your phone number to receive SMS notifications.
        
# Usage
To run the Cheap Flight Finder application, navigate to the project directory in your terminal and run the command python main.py. The program will search for the cheapest flights to the locations listed in your Google Sheet and send an SMS notification to your phone if a flight is found that is cheaper than your predefined price.

# Contributing
If you would like to contribute to the Cheap Flight Finder project, please open an issue or submit a pull request on GitHub.
