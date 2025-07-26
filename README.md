Generate random music bingo cards using your Spotify playlists.

To run this yourself:
 - Clone this repo
 - Determine an FQDN that you're going to serve it at. Port 80 and 443 must be accessible to it from the internet. Register it in DNS.
 - Go to https://developer.spotify.com/dashboard.
   - Create a new App
     - App Name: bingo-card-creator (or whatever you want)
     - Description: whatever you want
     - Redirect URLs: https://<YOUR_FQDN>/spotify/callback/
     - Which API/SDKs are you planning to use? Web API
     - Save
   - Copy the spotify-app.env.template to spotify-app.env and edit it
     to put in your Client ID and Secret and your FQDN.
     For the DJANGO_SECRET_KEY, do something like go to https://www.random.org/strings/?num=1&len=32&digits=on&upperalpha=on&loweralpha=on&unique=on&format=html&rnd=new and get a random string.
 - Pull the docker images (`docker compose pull`) or build it yourself (`docker compose build`):
 - Start the containers (`docker compose up -d`)
 - Point your browser at `https://<YOUR_FQDN>/`

To see it work, go to https://spotify.bingo-list.com

FYI, if you print out the cards, make sure you enable printing the background. Otherwise the star in the middle square will not show up.
