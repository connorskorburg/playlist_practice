from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('sign_in', views.sign_in),
    path('search_track', views.search_track),
    path('track_results', views.track_results),
    path('new_releases', views.new_releases),
    path('show_profile', views.show_profile),
    path('callback', views.callback),
    path('get_playlists', views.get_playlists),
    path('new_playlist', views.new_playlist),
    path('create_playlist', views.create_playlist),
    path('add_song_to_playlist/<str:track_id>', views.add_song_to_playlist),
    path('new_song_in_playlist', views.new_song_in_playlist),
]
