from dotenv import dotenv_values
from movie import Movie
from ratings import Ratings
import requests

config = dotenv_values('.env')

API_KEY = config["API_KEY"]
api_url = 'https://imdb-api.com/en/API/'

def __call_api(endpoint, expressions, base_url=api_url, api_key=API_KEY):
    data = requests.get(base_url + endpoint + '/' + api_key + '/' + expressions)
    return data.json()

def search_movie(search):
    return __call_api('searchmovie', search)

def get_title(id):
    return __call_api('title', id)

def get_images(id):
    return __call_api('images', id)

def top_250_movies():
    return __call_api('top250movies', '')['items']

def get_description(id):
    pass

def get_ratings(id):
    return __call_api('ratings', id)

def youtube_trailer(id):
    return __call_api('youtubetrailer', id)

def ratings_from_id(id):
    ratings = get_ratings(id)
    return Ratings(
        imdb=ratings['imDb'],
        metacritic=ratings['metacritic'],
        rotten_tomatoes=ratings['rottenTomatoes']
    )

def movie_from_id(id):
    title = get_title(id)['title']
    thumbnail = get_images(id)['items'][0]['image']
    description = get_description(id)
    trailer = youtube_trailer(id)
    return Movie(
        id=id,
        title=title,
        thumbnail=thumbnail,
        description=description,
        length=0,
        youtube_trailer=trailer,
        ratings=vars(ratings_from_id(id))
    )