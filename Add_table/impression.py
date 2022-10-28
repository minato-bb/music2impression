import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

def getTrackIDs(user, playlist_id):
    ids = []
    client_id = 'b9fe370636f84fd0842758f0d48fd6d7'
    client_secret = '0c3cfec97b36433e96b666d6e7a3b00a'

    client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, language='ja')

    playlist = sp.user_playlist(user, playlist_id)
    while playlist['tracks']['next']:
        for item in playlist['tracks']['items']:
            track = item['track']
            ids.append(track['id'])
        playlist['tracks'] = sp.next(playlist['tracks'])
    else:
        for item in playlist['tracks']['items']:
            track = item['track']
            ids.append(track['id'])
    return ids


#df作成
def getTrackFeatures(id):
    client_id = 'b9fe370636f84fd0842758f0d48fd6d7'
    client_secret = '0c3cfec97b36433e96b666d6e7a3b00a'
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, language='ja')

    meta = sp.track(id)
    features = sp.audio_features(id)

    # data
    name = meta['name']
    artist = meta['album']['artists'][0]['name']
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    valence = features[0]['valence']

    track = [name, artist, danceability, acousticness, energy, liveness, loudness, speechiness, tempo, valence]
    return track

def make_df(ids):
    # loop over track ids
    tracks = []
    for i in range(len(ids)):
        time.sleep(.5)
        track = getTrackFeatures(ids[i])
        tracks.append(track)
        if i % 100 == 0:
            print(i)

    df = pd.DataFrame(tracks, columns = ['name', 'artist', 'danceability', 'acousticness', 'energy', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence'])
    

    return df