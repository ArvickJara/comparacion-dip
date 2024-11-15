from proveedor_publicaciones import ProveedorPublicaciones


class ServicioBaseDatosJson(ProveedorPublicaciones):
    def obtener_publicaciones(self):
        return [
            {"userId": 2, "id": 3, "title": "De archivo JSON",
                "body": "Publicación simulada desde JSON."}
        ]
