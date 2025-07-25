from .dao.firebase.firebaseDAOFactory import FirebaseDAOFactory
from .apiexterna.spotify.spotify import Spotify
from .dto.songDTO import SongsDTO, SongDTO
from .dto.artistDTO import ArtistsDTO, ArtistDTO    # Código Examen
class Model ():

    def __init__(self):
        pass
        self.factory = FirebaseDAOFactory()
        self.daoSong = self.factory.getSongDao()
        self.daoArtist = self.factory.getArtistDao()    # Código Examen
        self.spotify = Spotify()

    def get_songs(self):
        mySongsDTO = SongsDTO()
        songs = self.daoSong.get_songs()

        for s in songs:
            #song_data = s # (Local)
           # Crear un objeto SongDTO con los datos de la canción
            song_data = s.to_dict()
            song_dto = SongDTO()
            song_dto.id = s.id  # (Firestore)
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

#Código Exámen
    def get_latest_songs(self, limit=10):
        mySongsDTO = SongsDTO()
        songs = self.daoSong.get_latest_songs(limit)

        for s in songs:
            song_data = s.to_dict()
            song_dto = SongDTO()
            song_dto.id = s.id
            song_dto.title = song_data.get("title", "")
            song_dto.author = song_data.get("author", "")
            song_dto.album = song_data.get("album", "")
            song_dto.musicgenre = song_data.get("musicgenre", "")
            song_dto.duration = song_data.get("duration", 0)
            song_dto.price = song_data.get("price", 0.0)
            song_dto.rating = song_data.get("rating", 0)
            song_dto.release = song_data.get("release", "")
            mySongsDTO.insertSong(song_dto.songdto_to_dict())

        return mySongsDTO.songlist_to_json()


# Código Examen
    def get_artists(self):
        myArtistsDTO = ArtistsDTO()
        artists = self.daoArtist.get_artists()

        for a in artists:
            artist_data = a.to_dict()
            artist_dto = ArtistDTO()
            artist_dto.id = a.id  # (Firestore)
            artist_dto.name = artist_data.get("name", "")
            artist_dto.song_number = artist_data.get("song_number", "")


            myArtistsDTO.insertArtist(artist_dto.artistdto_to_dict())
        return myArtistsDTO.artistlist_to_json()