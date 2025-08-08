import requests
import random
import webbrowser

def RandomImg():

    rand = random.randint(0,1)
    if rand == 1 :
        api_key = "soovE4x4ZgJ13zxU1PYOQaOthuRlKGgKsAkwlcxVokCAPX4VCJ6e2dcflhZOceeV"
        url = "https://api.thecatapi.com/v1/images/search"

    else :
        # api_key = ""
        url = "https://api.thedogapi.com/v1/images/search"

    response = requests.get(url).json()
    print(response)
    webbrowser.open(response[0]['url'])

while True:
    RandomImg()

    status = input("Next (y/n) ? ")
    if status == "y":
        pass
    else:
        break

