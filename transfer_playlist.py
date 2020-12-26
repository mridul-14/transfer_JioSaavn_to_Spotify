import requests
from bs4 import BeautifulSoup
from random import randint
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

USERNAME = <your username>
SCOPE = 'playlist-modify-public'
CLIENT_ID = <your client ID>
CLIENT_SECRET = <your client key>
REDIRECT_URL = 'http://localhost:8080' # this needs to be same as in the Spotify app (created while registering to use Spotify API)
PLAYLIST = 'Jio_Spotify' # name of playlist on Spotify
all_tracks = list()

''' Can remove headers_list'''
headers_list = [
    # Firefox 77 Mac
     {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Firefox 77 Windows
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.co.in/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    },
    # Chrome 83 Mac
    {
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.co.in/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    },
    # Chrome 83 Windows 
    {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
]

def GetPlaylistID(username, playlist_name):
    playlist_id = ''
    playlists = sp.user_playlists(user=username, limit=50)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
    return playlist_id

def addSongsToPlaylist(song_list):
    ID = GetPlaylistID(USERNAME, PLAYLIST)
    try:
        sp.user_playlist_add_tracks(user=USERNAME, playlist_id=ID, tracks=song_list, position=None)
    except:
        print('Could not add ', _, ' to playlist')

url = <URL to your Saavn playlist>
page = requests.get(url, headers=headers_list[randint(0, 3)])
soup = BeautifulSoup(page.content, 'lxml')

token = util.prompt_for_user_token(USERNAME, SCOPE, client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URL) 
sp = spotipy.Spotify(auth=token)
sp.user_playlist_create(USERNAME, name=PLAYLIST)

tag = soup.find('section', class_='u-margin-bottom-large@sm')
for _ in tag.find_all('figcaption', class_='o-flag__body'):
    song_name = _.h4.a.text
    artist_tag = _.find('p', class_='u-centi u-ellipsis u-color-js-gray-alt-light u-margin-right@sm u-margin-right-none@lg')
    artist_names = artist_tag.text.strip().replace('\n', '')
    query = song_name+' '+artist_names
    try:
        track_id = sp.search(q=query, type='track')
        track_id = track_id['tracks']['items'][-1]['uri']
        all_tracks.append(track_id)
    except:
        print('Song not found: ', query)

addSongsToPlaylist(all_tracks)
