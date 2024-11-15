from servicio_base_datos_local import ServicioBaseDatosLocal
from no_DIP.servicio_base_datos_json import ServicioBaseDatosJson
from servicio_api_web import ServicioApiWeb
from servicio_publicaciones import ServicioPublicaciones


def main():
    # Cambiar aquí para usar otra implementación
    # Cambiar a ServicioBaseDatosJson o ServicioApiWeb o ServicioBaseDatosLocal
    proveedor = ServicioBaseDatosJson()
    servicio_publicaciones = ServicioPublicaciones(proveedor)

    publicaciones = servicio_publicaciones.obtener_publicaciones()
    print("Publicaciones obtenidas:")
    for publicacion in publicaciones:
        print(publicacion)


if __name__ == "__main__":
    main()
