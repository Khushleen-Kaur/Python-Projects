#Using API

import datetime as dt
import requests

api_key = "de42713133714b409df152022250808"
location = input("Enter Location : ")
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"

response = requests.get(url).json()

# print(response)

print(f"Temperature(in celcius) : {response['current']['temp_c']}")
print(f"Temperature(in fahrenheit) : {response['current']['temp_f']}")
print(f"Temperature feels like(in celcuis) : {response['current']['feelslike_c']}")
print(f"Condition : {response['current']['condition']['text']}")
print(f"Humidity : {response['current']['humidity']}")

