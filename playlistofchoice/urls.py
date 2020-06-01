from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('sign_in', views.sign_in),
    path('search_track', views.search_track),
    path('track_results', views.track_results),
    path('new_releases', views.new_releases),
    path('show_profile', views.show_profile),
    path('get_token', views.get_token),
    path('callback', views.callback),
    path('get_playlists', views.get_playlists),
]
