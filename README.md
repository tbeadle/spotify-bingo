Generate random music bingo cards using your Spotify playlists.

To run this yourself:
 - Clone this repo
 - Go to https://developer.spotify.com/dashboard.
   - Create a new App
     - App Name: bingo-card-creator (or whatever you want)
     - Description: whatever you want
     - Redirect URLs: https://127.0.0.1/spotify/callback/
     - Which API/SDKs are you planning to use? Web API
     - Save
   - Copy the spotify-app.env.template to spotify-app.env and edit it
     to put in your Client ID and Secret
     For the DJANGO_SECRET_KEY, do something like go to https://www.random.org/strings/?num=1&len=32&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new and get a random string.
 - Generate a self-signed cert and put the cert and key in nginx/certs/selfsigned.crt and selfsigned.key
   ```
   mkdir -p nginx/certs && \
   openssl req -x509 -newkey rsa:4096 -nodes -keyout nginx/certs/selfsigned.key -out nginx/certs/selfsigned.crt -sha256 -days 3650 
   ```
 - Pull the docker image (`docker compose pull`) or build it yourself (`docker compose build`):
 - Start the containers (`docker compose up`)
 - Point your browser at `https://127.0.0.1/`