from .dao.firebase.firebaseDAOFactory import FirebaseDAOFactory
from .apiexterna.spotify.spotify import Spotify
from .dto.songDTO import SongsDTO, SongDTO
class Model ():

    def __init__(self):
        pass
        self.factory = FirebaseDAOFactory()
        self.daoSong = self.factory.getSongDao()
        self.spotify = Spotify()

    def get_songs(self):
        # return None
        mySongsDTO = SongsDTO()
        songs = self.daoSong.get_songs()
        for s in songs:
            song_data = s # (Local)
           # Crear un objeto SongDTO con los datos de la canción
            song_dto = SongDTO()
           # song_dto.id = doc.id  # (Firestore)
            song_dto.title = song_data.get("id", "") # (Local)
            song_dto.title = song_data.get("title", "")
            song_dto.author = song_data.get("author", "")
            song_dto.album = song_data.get("album", "")
            song_dto.musicgenre = song_data.get("musicgenre", "")
            song_dto.duration = song_data.get("duration", 0)
            song_dto.price = song_data.get("price", 0.0)
            song_dto.rating = song_data.get("rating", 0)
            song_dto.release = song_data.get("release", "")
            mySongsDTO.insertSong(song_dto.songdto_to_dict())  # Agregar la canción a la lista
        return mySongsDTO.songlist_to_json()
    
    def get_songs_by_artist(self, artist_name):
        tracks = self.spotify.get_songs_by_artist(artist_name) # Si quisiera hacer la llamada a mi bbdd solo tendría que modificar esta línea
        # Generacion DTO
        my_songs_dto = SongsDTO()
        for track in tracks:
            print(track["id"])
            song = SongDTO()
            album = track["album"]["name"]
            song.set_album(album)
            authorship = ""
            for author in track["artists"]:
                print(author)
                authorship = authorship + author["name"] + ", "
            song.set_author(authorship[:-1]) # Eliminar la coma
            song.set_duration(track["duration_ms"])
            song.set_id(track["id"])
            #song.set_musicgenre()
            song.set_rating(track["popularity"])
            release = track["album"]["release_date"]
            song.set_release(release)
            song.set_title(track["name"])
            my_songs_dto.insertSong(song.songdto_to_dict())
        return my_songs_dto.songlist_to_json()

