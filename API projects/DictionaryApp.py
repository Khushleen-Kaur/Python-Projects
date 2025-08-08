import requests

word = input("Enter word : ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url).json()

print(f"Meaning : {response[0]['meanings'][0]['definitions'][0]['definition']}")
print(f"Parts of speech : {response[0]['meanings'][0]['partOfSpeech']}")



