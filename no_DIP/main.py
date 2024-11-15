from servicio_publicaciones import ServicioPublicaciones

def main():
    servicio_publicaciones = ServicioPublicaciones()

    # Cambiar manualmente la fuente de datos
    print("Datos desde base de datos local:")
    publicaciones_local = servicio_publicaciones.obtener_publicaciones_desde_local()
    for publicacion in publicaciones_local:
        print(publicacion)
"""
    print("\nDatos desde archivo JSON:")
    publicaciones_json = servicio_publicaciones.obtener_publicaciones_desde_json()
    for publicacion in publicaciones_json:
        print(publicacion)

    print("\nDatos desde API web:")
    publicaciones_api = servicio_publicaciones.obtener_publicaciones_desde_api()
    for publicacion in publicaciones_api[:2]:  # Mostrar solo las primeras dos publicaciones
        print(publicacion) """

if __name__ == "__main__":
    main()
