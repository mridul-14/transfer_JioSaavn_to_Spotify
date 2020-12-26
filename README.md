# transfer_JioSaavn_to_Spotify
This script can be used to transfer JioSaavn playlist to Spotify.

Spotify is 'the' best music streaming app. When I made the switch from Saavn to Spotify, I also had to transfer my playlists and hence this I wrote this script.I couldn't find a service that doesn't take my data and does the job for me.

Prerequisites:
1. Python modules-
  a. requests
  b. BeautifulSoup4
  c. random (optional, used for header rotation while testing.)
  d. spotipy
2. Spotify Client ID and Secret Key - Check here on how to get them (https://developer.spotify.com/documentation/web-api/)
3. A public JioSaavn playlist - URL

So basically what this script does is to scrape Song & Artist names from your Saavn playlist then it creates a new playlist in Spotify and adds all the songs.
If there's a song that is not available in Spotify for some reason; you'll see a message in the console, same goes for the situation when there was some error while adding a song to the playlist.

Things to be noted-
Like I mentioned before, your playlist on Saavn will be public (didn't test with private) and the playlist created on Spotify will be public as well (can be changed to private later).

You need to have a client id, secret key beforehand (both are simple to get). You can leave REDIRECT_URL as it is, for the first run, it will open for registration.
You don't need to login into Saavn so none of your data is compromised.
