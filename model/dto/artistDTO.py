# Código Examen
import json

class ArtistsDTO():
    def __init__(self):
        self.artistlist = []

    def insertArtist(self, elem):
        self.artistlist.append(elem)

    def artistlist_to_json(self):
        return json.dumps(self.artistlist)


class ArtistDTO():
    def __init__(self):
        self.name = None
        self.song_number = None
        self.id = None

    def is_Empty(self):
        return (self.name is None and self.song_number is None and self.id is None)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_song_number(self):
        return self.song_number

    def set_song_number(self, song_number):
        self.song_number = song_number

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def artistdto_to_dict(self):
        return {
            "name": self.name,
            "song_number": self.song_number,
            "id": self.id,
        }