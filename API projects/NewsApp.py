import datetime as dt
import requests

api_key = "da52169a415d407cb8fcfa5e244798e1"
country = input("Enter country : ").strip().lower()
category = input("Enter category for news : ").strip().lower()

url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}"

response = requests.get(url).json()
if(response['totalResults']==0):
    print("No results found!")

else:
    for article in response['articles']:
        print(article['title'],f"~{article['author']}")


        soovE4x4ZgJ13zxU1PYOQaOthuRlKGgKsAkwlcxVokCAPX4VCJ6e2dcflhZOceeV