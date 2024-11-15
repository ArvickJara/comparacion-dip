from abc import ABC, abstractmethod
from typing import List, Dict


class ProveedorPublicaciones(ABC):
    @abstractmethod
    def obtener_publicaciones(self) -> List[Dict]:
        """Obtiene una lista de publicaciones."""
        pass
