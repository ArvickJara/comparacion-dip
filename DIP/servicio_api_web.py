import requests
from proveedor_publicaciones import ProveedorPublicaciones


class ServicioApiWeb(ProveedorPublicaciones):
    def obtener_publicaciones(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()
