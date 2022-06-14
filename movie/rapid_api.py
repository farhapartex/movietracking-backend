import requests
from django.conf import settings
from rest_framework import status
from movie import models


def get_rapid_api_header(rapid_api_key: str):
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": settings.RAPID_API_HOST
    }

    return headers


def map_movie_data(movie):
    data = {**movie}
    imdb_id = movie['imdbID']
    instance = models.Movie.get_instance({"imdb_id": imdb_id})
    data["is_new"] = True if instance is None else False
    data["is_favorite"] = instance.is_favorite if instance else False
    data["is_watched"] = instance.is_watched if instance else False
    return data


def search_movie_by_title(title: str, rapid_api_key: str):
    querystring = {"s": title, "r": "json", "page": "1"}
    response = requests.request("GET", settings.RAPID_API_URL, headers=get_rapid_api_header(rapid_api_key), params=querystring)
    if response.status_code == status.HTTP_403_FORBIDDEN:
        return status.HTTP_403_FORBIDDEN, None

    res_data = response.json()
    if res_data['Response'] != "True":
        return status.HTTP_200_OK, []

    movies = res_data['Search']
    return status.HTTP_200_OK, list(map(map_movie_data, movies))


def search_movie_by_imdb_id(imdb_id: str, rapid_api_key: str):
    querystring = {"r": "json", "i": imdb_id}
    response = requests.request("GET", settings.RAPID_API_URL, headers=get_rapid_api_header(rapid_api_key), params=querystring)
    if response.status_code == status.HTTP_403_FORBIDDEN:
        return status.HTTP_403_FORBIDDEN, None

    movie = response.json()

    if movie['Response'] != "True":
        return status.HTTP_200_OK, {}

    return status.HTTP_200_OK, movie
