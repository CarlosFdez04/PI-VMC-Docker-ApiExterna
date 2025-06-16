from fastapi.templating import Jinja2Templates
from fastapi import Request
import json
templates = Jinja2Templates(directory="view/templates") # Es esta ruta porque
# # estamos ejecutando desde ejemplo_canciones

class View():
    def __init__(self):
        pass
    def get_index_view(self, request: Request):
        return templates.TemplateResponse("index.html", {"request" : request})
    def get_songs_view(self, request: Request, songs):
        songs_list = json.loads(songs)
        return templates.TemplateResponse("songs.html", {"request" :request, "songs" : songs_list})
