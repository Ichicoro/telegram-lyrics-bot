import json, os

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class geniuslyrics:
    def __init__(self, client_access_token):
        self.client_access_token = client_access_token


    # use the Genius API to search for a song and retrieve the URL
    def search_song_url(self, song_query):
        # Generate search request
        response = requests.get("http://api.genius.com/search?access_token=" + self.client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        search_json = json.loads(response.text)
        print(search_json)
        song_url = search_json['response']['hits'][0]['result']['url']
        return song_url


    def search_title(self, song_query):
        # Generate search request
        response = requests.get("http://api.genius.com/search?access_token=" + self.client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        search_json = json.loads(response.text)
        print(search_json)
        print("printo i risultati")
        print(search_json['response']['hits'][0]['result'])
        song_title = search_json['response']['hits'][0]['result']['full_title']
        return song_title


    def search(self, song_query):
        # Generate search request
        response = requests.get("http://api.genius.com/search?access_token=" + self.client_access_token + "&q=" + song_query , headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
        search_json = json.loads(response.text)
        print(search_json)
        return search_json['response']['hits'][0]

    # scrape a Genius song page for the full lyrics
    def scrape(self, song_url):
        print("Retrieving lyrics from " + song_url)

        # Get raw lyrics for first song result
        response = requests.get(song_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

        # Clean up html
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.find("div", class_="lyrics")
        lyrics = soup.get_text().strip()

        return lyrics


def getSongByName(song_name):
    # genius = geniuslyrics(CLIENT_ACCESS_TOKEN)
    gl = geniuslyrics(os.environ["GENIUS_ACCESS_TOKEN"])
    result = gl.scrape(gl.search_song_url(song_name))
    print(result)
    return result

def getSongData(song_name):
    gl = geniuslyrics(os.environ["GENIUS_ACCESS_TOKEN"])
    result = gl.search(song_name)
    return result

def getSongTitle(song_name):
    gl = geniuslyrics(os.environ["GENIUS_ACCESS_TOKEN"])
    result = gl.search_title(song_name)
    return result
