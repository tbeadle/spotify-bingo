import random
from io import BytesIO
from django import forms
from django.shortcuts import redirect, render
from django.http import FileResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPE = "playlist-read-private playlist-read-collaborative"

class PlaylistSelectionForm(forms.Form):
    playlist_id = forms.ChoiceField(label="Choose a playlist")
    title = forms.CharField(label="Title for cards", max_length=64)
    num_cards = forms.IntegerField(min_value=1, initial=1, label="Number of Bingo cards")

def get_spotify_oauth(request):
    return SpotifyOAuth(
        settings.SPOTIFY_CLIENT_ID,
        settings.SPOTIFY_CLIENT_SECRET,
        f"https://{request.get_host()}" + reverse('spotify_callback'),
        scope=SCOPE
    )
def login_spotify(request):
    auth_url = get_spotify_oauth(request).get_authorize_url()
    return redirect(auth_url)

def spotify_callback(request):
    code = request.GET.get('code')
    token_info = get_spotify_oauth(request).get_access_token(code)
    request.session['token_info'] = token_info
    return redirect('generate_bingo')

def home(request):
    return render(request, 'bingo/home.html')

def generate_bingo(request):
    token_info = request.session.get('token_info')
    if not token_info:
        return redirect('login_spotify')

    sp = spotipy.Spotify(auth=token_info['access_token'])

    playlists = sp.current_user_playlists(limit=50)
    playlist_choices = [(pl['id'], pl['name']) for pl in sorted(playlists['items'], key=lambda pl: pl['name'])]
    form = PlaylistSelectionForm(request.POST if request.method == "POST" else None)
    form.fields['playlist_id'].choices = playlist_choices

    if not (request.method == "POST" and form.is_valid()):
        return render(request, 'bingo/select_playlist.html', {'form': form})
    playlist_id = form.cleaned_data['playlist_id']
    num_cards = form.cleaned_data['num_cards']

    tracks = []
    results = sp.playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track and track['name']:
                tracks.append(track['name'])
        if results.get('next'):
            results = sp.next(results)
        else:
            results = None

    if len(tracks) < 24:
        return render(request, 'bingo/error.html', {'message': 'Not enough tracks to create a bingo card.'})

    bingo_cards = []
    for _ in range(num_cards):
        selected = random.sample(tracks, 24)
        selected.insert(12, "FREE")
        grid = [selected[i:i+5] for i in range(0, 25, 5)]
        bingo_cards.append(grid)

    ctx = {'bingo_cards': bingo_cards, 'title': form.cleaned_data['title']}
    return render(request, 'bingo/bingo_cards.html', ctx)