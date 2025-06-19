#Código Examen
from ...interfaceDAOArtist import InterfaceArtistDAO

class FirebaseArtistDAO(InterfaceArtistDAO):

    def __init__(self, collection):
        self.collection = collection
    
    def get_artists(self):
        try:
            query = self.collection.order_by("song_number", direction="ASCENDING").stream() # (Firebase)
            #query = self.collection # (Local)
            # Tal vez pueda ser necesario realizar un pre procesamiento del resultado de la consulta para devolver
            # una información al modelo homogénea
            # print(query)
        except Exception as e:
            print(e)
        
        return query
