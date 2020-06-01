from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys
import requests
import base64
import datetime

# Create your views here.

# RENDER TEMPLATES

def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'index.html')

def sign_in(request):
    username = request.POST['username']
    request.session['username'] = username
    client_id = '93d03c51a99146ed992ca0175f68674b'
    client_secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    return redirect(f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope=playlist-modify-public&redirect_uri=http://localhost:8000/callback')

def callback(request):
    client_id = '93d03c51a99146ed992ca0175f68674b'
    client_secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    # print("REQUEST",request.GET['code'])
    code = request.GET['code']
    token_url =  'https://accounts.spotify.com/api/token'
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())
    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        'redirect_uri': 'http://localhost:8000/callback',
    }
    token_headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"
    }
    r = requests.post(token_url, data=token_data, headers=token_headers)
    print(r.json())
    print("TOKEN IS HERE:", r.json()['access_token'])
    valid_request = r.status_code in range(200, 299)
    if valid_request:
        token_response_data = r.json()
        now = datetime.datetime.now()
        access_token = token_response_data['access_token']
        request.session['access_token'] = access_token
        expires_in = token_response_data['expires_in']
        request.session['expires_in'] = expires_in
        expires = now + datetime.timedelta(seconds=expires_in)
        did_expire = expires < now

    return redirect('/')

def get_playlists(request):
    if request.session['username']:
        token = request.session['access_token']
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(request.session['username'])
        playlists_list = []
        for i in playlists['items']:
            playlists_list.append(
                {
                    'name': i['name'],
                    'description': i['description'],
                    'playlist_id': i['id'],
                    'image': i['images'][0]['url'],
                }
            )
        context = {
            'playlists_list': playlists_list
        }
        return render(request, 'playlists.html', context)
        
    else:
        request.session['username'] == False
        return render(request, 'playlists.html')
# track results
def track_results(request):
    track_info_length = len(request.session['track_info_list'])
    context = {
        'track_info_list': request.session['track_info_list'],
        'track_searched': request.session['track_searched'],
        'track_info_length': track_info_length,
    }
    return render(request, 'track_results.html', context)

# handling POST DATA

# search for a track
def search_track(request):
    track = request.POST['track']
    if track == '':
        return redirect('/show_tracks')
    cid = '93d03c51a99146ed992ca0175f68674b'
    secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    track_results = sp.search(q=track, type='track', limit=15)
    track_info_list = []
    for i in track_results['tracks']['items']:
        track_info_list.append(
            {
                'image': i['album']['images'][0]['url'],
                'artist': i['artists'][0]['name'],
                'track': i['name'],
                'track_id': i['id'],
                'explicit': i['explicit'],
            }
        )    
    # print("TRACK INFO", track_info_list)
    request.session['track_info_list'] = track_info_list
    request.session['track_searched'] = track

    return redirect('/track_results')


def new_releases(request):
    cid = '93d03c51a99146ed992ca0175f68674b'
    secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.new_releases(country=None, limit=20, offset=0)
    new_realeases_list = []
    for i in results['albums']['items']:
        new_realeases_list.append(
            {
                "artist": i['artists'][0]['name'],
                "album_id": i['id'],
                "album": i['name'],
                "image_url": i['images'][0]['url'],
            }
        )
    context = {
        'new_releases_list': new_realeases_list
    }
    return render(request, 'new_releases.html', context)

def show_lyrics(request):
    secret = 'G5IWRkk5VKlZAilHFLawRsxIChzwPFo6KqWTQvzEnO1_jSw-XoHxmkHsnc12Q12KGPIX7qRpu5p52d2Bud0R-A'
    client_id = 'Gi70YVXzHfuYabtUHrtCxyUWmbn6J0ZEBXy0Cb9cr0k7mM_K8GMju9poTt0NTrSV'

def show_profile(request):
    cid = '93d03c51a99146ed992ca0175f68674b'
    secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    
    return render(request, 'profile.html')


def get_token(request):
    code = 'AQAWfTk-j5TNXU_DFktvxjvKAfzC94If3filKM9WAA3XnLcmcHgeSg3Ji7_-QrR_mkccAXpRmocamgKQHHMPQdwiOKpmttsABbGOF_BshXU7j2Df59ro_NS8-JKr5bfs75Wj0RcB4BYtKimtig2tLtjMfxxlVCDtyWqmdhjRiqTy7iYpAVKw8vj5kCrbCV8lxQ'
    return redirect(f'https://accounts.spotify.com/api/token&grant_type=authorization_code&code={code}&redirect_uri=http%3A%2F%2Flocalhost%3A8000')