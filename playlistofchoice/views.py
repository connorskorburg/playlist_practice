from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import sys

# Create your views here.

# RENDER TEMPLATES

def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'index.html')

def sign_in(request):
    username = request.POST['username']
    cid = '93d03c51a99146ed992ca0175f68674b'
    secret = '92a2119255fb489bbfe6e2a054f8c4b5'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    token = util.prompt_for_user_token(username, scope='playlist-modify-public', client_id=cid, client_secret=secret, redirect_uri= 'localhost:8000')
    return redirect('/')

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