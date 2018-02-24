import spotipy
import spotipy.util as util
import sys

username = 'vishal.ponugoti'
# username = 'bubbleballoonbee'
scope = 'user-library-read user-read-private playlist-modify-private playlist-modify-public user-top-read'

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks()
    for item in results['items']:
        track = item
        print(track['name'], '-', track['artists'][0]['name'])
else:
    print("Can't get token for", username)
