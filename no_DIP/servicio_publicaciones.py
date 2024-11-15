class ServicioPublicaciones:
    def __init__(self):
        self.publicaciones = []

    def obtener_publicaciones_desde_local(self):
        from servicio_base_datos_local import ServicioBaseDatosLocal
        servicio = ServicioBaseDatosLocal()
        self.publicaciones = servicio.obtener_publicaciones()
        return self.publicaciones

    def obtener_publicaciones_desde_json(self):
        from servicio_base_datos_json import ServicioBaseDatosJson
        servicio = ServicioBaseDatosJson()
        self.publicaciones = servicio.obtener_publicaciones()
        return self.publicaciones 

    def obtener_publicaciones_desde_api(self):
        from servicio_api_web import ServicioApiWeb
        servicio = ServicioApiWeb()
        self.publicaciones = servicio.obtener_publicaciones()
        return self.publicaciones 
