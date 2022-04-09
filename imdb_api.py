from dotenv import dotenv_values
import requests

config = dotenv_values('.env')

API_KEY = config["API_KEY"]
api_url = 'https://imdb-api.com/en/API/'

def __call_api(endpoint, expressions, base_url=api_url, api_key=API_KEY):
    data = requests.get(base_url + endpoint + '/' + api_key + '/' + expressions)
    return data.json()

def search_movie(search):
    return __call_api('searchmovie', search)

def ratings(id):
    return __call_api('ratings', id)

def youtube_trailer(id):
    return __call_api('youtubetrailer', id)