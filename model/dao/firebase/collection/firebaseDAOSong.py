from ...interfaceDAOSong import InterfaceSongDAO

class FirebaseSongDAO(InterfaceSongDAO):

    def __init__(self, collection):
        self.collection = collection
    
    def get_songs(self):
        try:
            query = self.collection.stream() # (Firebase)
            #query = self.collection # (Local)
            # Tal vez pueda ser necesario realizar un pre procesamiento del resultado de la consulta para devolver
            # una información al modelo homogénea
#             print(query)
        except Exception as e:
            print(e)
        
        return query
    
    def get_songs_by_artist(self, name):
        # Como estamos heredando de la interfaz DAO Song, debemos de tener implementados los métodos 
        # que se han definido
        pass

#Código Examen
    def get_latest_songs(self, limit=10):
        try:
            query = self.collection.order_by("release", direction="DESCENDING").limit(limit).stream()
            return query
        except Exception as e:
            print("Error al obtener las canciones más recientes:", e)
            return []
