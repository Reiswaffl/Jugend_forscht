import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

username = "reiswaffl123"

token = util.prompt_for_user_token(username,scope,client_id='678a44df3488479d97bcd9995f4d419d',client_secret='aa5a13cac9b84027a72ce7ad6e36e182',redirect_uri='http://localhost:8888/callback/')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print track['name'] + ' - ' + track['artists'][0]['name']
else:
    print "Can't get token for", username