import requests

class ServicioApiWeb:
    def obtener_publicaciones(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()
