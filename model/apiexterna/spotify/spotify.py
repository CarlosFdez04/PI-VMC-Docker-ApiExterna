# #Ctrl + K, CTRL + U
from ...dao.interfaceDAOSong import InterfaceSongDAO
import requests
import base64
class Spotify(InterfaceSongDAO):
    def __init__(self):
        self.CLIENT_ID = "9311a46e26a44cf499ae30343e72065d"
        self.CLIENT_SECRET = "2490ec9c87404ec4afbdd4f8070c79d5"
        self.token = ""
    
    def update_spotify_token(self):
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + base64.b64encode(f"{self.CLIENT_ID}:{self.CLIENT_SECRET}".encode()).decode()
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post(url, headers=headers, data=data)
        self.token = response.json().get("access_token")
    

    def get_artist_id(self, artist_name):
        url = f"https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"q": artist_name, "type": "artist", "limit": 1}

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if data["artists"]["items"]:
            return data["artists"]["items"][0]["id"]
        else:
            return None
    
    def get_songs_by_artist(self, artist_name):
        self.update_spotify_token() # Se debería de gestionar el token para comprobar el tiempo de expiración 
        artist_id = self.get_artist_id(artist_name)
        if not artist_id:
            return f"No se encontró el artista: {artist_name}"

        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
        headers = {"Authorization": f"Bearer {self.token}"}
        params = {"market": "US"}

        response = requests.get(url, headers=headers, params=params)
        tracks = response.json()["tracks"]
        return tracks
    
    def get_songs(self):
        # Como estamos heredando de la interfaz DAO Song, debemos de tener implementados los métodos 
        # que se han definido
        pass

    #Código Exámen
    def get_latest_songs(self, limit=10):
        raise NotImplementedError("Spotify no implementa este método")

        
