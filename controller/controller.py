from fastapi import FastAPI, Request
from view.view import View
from model.model import Model
# Inicializamos la app

app = FastAPI()

view = View()
model = Model()

# Código 1
@app.get("/")
def index(request: Request): 
   #return {"message" : "HELLO WORLD! :)"}
    return view.get_index_view(request)

# Código 2 
@app.get("/getsongs", description="Hola esto es una descripcion")
def getsongs(request: Request):
    # return {"message" : "Canciones"}
    songs = model.get_songs() # JSON
    return view.get_songs_view(request,songs)

# Código 3 API Externa
@app.get("/search-songs-by-artist", description="Proceso para la búsqueda de las canciones de un artista haciendo uso de la api de Spotify")
def search_songs_by_artist(request: Request, artist: str):
    print(artist)
    songs =  model.get_songs_by_artist(artist) # Obtendremos el DTO
    return view.get_songs_view(request, songs)

# Código Exámen
@app.get("/latest-songs", description="Listado de las 10 canciones más recientes")
def latest_songs(request: Request):
    songs = model.get_latest_songs()
    return view.get_latest_songs_view(request, songs)


# Código Examen
@app.get("/getartists", description="Hola esto es una descripcion")
def getartists(request: Request):
    artists = model.get_artists() # JSON
    return view.get_artists_view(request,artists)