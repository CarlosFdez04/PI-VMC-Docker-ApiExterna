from abc import ABC, abstractmethod
from typing import List, Optional

class InterfaceSongDAO(ABC):

    @abstractmethod
    def get_songs(self):
        pass

    @abstractmethod
    def get_songs_by_artist(self, name):
        pass

#Código Examen
    @abstractmethod
    def get_latest_songs(self, limit=10):
        pass
