from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_spotify, name='login_spotify'),
    path('spotify/callback/', views.spotify_callback, name='spotify_callback'),
    path('bingo/', views.generate_bingo, name='generate_bingo'),
]
