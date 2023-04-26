import requests
from data_access import get_movies, get_movie_details

def sort_movies_by_id():
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in get_movies()]
    sorted_movies = sorted(movies, key=lambda x: x['id'])
    return sorted_movies

def get_movie_characters(movie_id):
    movie_details = get_movie_details(movie_id)
    characters = [requests.get(char_url).json()["name"] for char_url in movie_details["characters"]]
    return characters
