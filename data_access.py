import requests

movie_url = "https://swapi.dev/api/films/"

def get_movies():
    data = requests.get(movie_url).json()
    return data["results"]

def get_movie_details(movie_id):
    movie_details_url = f"{movie_url}{movie_id}/"
    movie_details = requests.get(movie_details_url).json()
    return movie_details
