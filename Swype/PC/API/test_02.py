import spotipy
import spotipy.oauth2 as oauth2
import spotilib
import win32gui


def get_info_windows():
    windows = []



    # Newer Spotify versions - create an EnumHandler for EnumWindows and flood the list with Chrome_WidgetWin_0s
    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
            windows.append(text)

    win32gui.EnumWindows(find_spotify_uwp, windows)
    print('Starting shit')
    while windows.count != 0:
        try:
            text = windows.pop()
            print(text)
        except:
            return "Error", "Nothing playing"
        try:
            artist, track = text.split(" - ", 1)
            print( artist, track )
        except:
            print('Error')
get_info_windows()
'''
def show_playlist(playlist):
    results = spotify.user_playlist(
        playlist['owner']['id'], playlist['id'], fields='tracks,next')

    tracks = results['tracks']
    show_tracks(tracks)


def show_tracks(tracks):
    n = 1
    while True:
        for item in tracks['items']:
            track = item['track']
            track_title = str(n) + '. '
            track_title += track['name'] + ' - ' + track['artists'][0]['name']
            print(track_title)
            n += 1
        # 1 page = 50 results
        # check if there are more pages
        if tracks['next']:
            tracks = spotify.next(tracks)
        else:
            break
credentials = oauth2.SpotifyClientCredentials(
        client_id="678a44df3488479d97bcd9995f4d419d",
        client_secret="aa5a13cac9b84027a72ce7ad6e36e182")

token = credentials.get_access_token()
print(token)
username = 'reiswaffl123'
if token:
    spotify = spotipy.Spotify(auth=token)
    playlists = spotify.user_playlists(username)
    check = 1

    while True:
        for playlist in playlists['items']:
            # in rare cases, playlists may not be found, so playlists['next']
            # is None. Skip these.
            if playlist['name'] is not None:
                print('')
                print('playlist:')
                playlist_title = playlist['name'] + ' - ' + str(playlist['tracks']['total'])
                playlist_title += ' tracks'
                print(playlist_title)
                show_playlist(playlist)
                check += 1
        if playlists['next']:
            playlists = spotify.next(playlists)
        else:
            break
else:
    print "Can't get token for", username
'''