from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('sign_in', views.sign_in),
    path('search_track', views.search_track),
    path('track_results', views.track_results),
    path('new_releases', views.new_releases),
]
