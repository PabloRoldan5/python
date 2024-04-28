import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
import plotly.express as px

#CONEXION A SPOTIFY
client_id="66707dbd25cd443ba60ec0ed41bece79"
client_secret="05f1c43b9eec4a718dec98b731f4d830"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

class Artista(object):
    def __init__(self):
        self.nombre = input("Introduzca nombre: ")

    def obtener_id_artista(self):
        results = sp.search(q=self.nombre,limit=1,type='artist')
        artist_id = results['artists']['items'][0]['id']
        return artist_id

class Album(object):
    def __init__(self, artista_id):
        self.artista_id = artista_id
    
    
     
    def buscar_albums_artista(self):
        listaAlbum = []
        albums = sp.artist_albums(artist_id=self.artista_id,album_type='single')
        for album in albums['items']:
             listaAlbum.append(album['name'])
        return listaAlbum
             
            
class Cancion(object):
    def __init__(self,artista_id):
        self.artista_id = artista_id
    
    def top_canciones(self):
        
        canciones = sp.artist_top_tracks(artist_id=self.artista_id)
        return canciones
        
  



