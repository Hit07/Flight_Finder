import requests

SHEETY_ENDPOINT = "https://api.sheety.co/cafbb767c733f083a83e1e17b207d123/flightDeals/users"
HEADER = {"Authorization": "Bearer hkshddnw35wbsjw6",
          'Content-Type': 'application/json'
          }

print("Welcome to Hitesh's Flight Club\n"
      "We find the best flight deals and email you.")

fname = input("What is your first name\n")
lname = input("what is your last name\n")
email = input("Enter your email\n")
confirm = input("Re-enter the email to confirm\n")
if email == confirm:
    data = {
        'user': {
            "firstName": fname,
            "lastName": lname,
            "email": email
        }
    }
    r = requests.post(url=SHEETY_ENDPOINT, headers=HEADER, json=data)
    print(r.text)
else:
    raise Exception("Entered mail doesn't match")