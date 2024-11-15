from proveedor_publicaciones import ProveedorPublicaciones
from typing import List, Dict


class ServicioPublicaciones:
    def __init__(self, proveedor: ProveedorPublicaciones):
        self.proveedor = proveedor

    def obtener_publicaciones(self) -> List[Dict]:
        return self.proveedor.obtener_publicaciones()
