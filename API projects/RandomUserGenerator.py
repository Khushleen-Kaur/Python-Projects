import webbrowser
import requests

url = "https://randomuser.me/api/"

response = requests.get(url).json()

print(f"Name : {response['results'][0]['name']['title']} {response['results'][0]['name']['first']} {response['results'][0]['name']['last']}")
print(f"Gender : {response['results'][0]['gender']}")
print(f"Age : {response['results'][0]['registered']['age']}")
print(f"Location : {response['results'][0]['location']['state']} , {response['results'][0]['location']['country']}")
print(f"E-mail : {response['results'][0]['email']}")
webbrowser.open(response['results'][0]['picture']['large'])