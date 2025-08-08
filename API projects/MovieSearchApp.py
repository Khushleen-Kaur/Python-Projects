import requests

api_key = "ad1a0393"
imdb_id = input("Enter valid IMDb ID : ")
movie_title = input("Enter a movie title : ")
url = f"http://www.omdbapi.com/?i={imdb_id}&t={movie_title}&apikey={api_key}"

response = requests.get(url).json()

print("Year : ",response['Year'])
print(f"Released date : {response['Released']}")
print(f"IMDb Rating : {response['imdbRating']}")
print(f"Plot : {response['Plot']}")