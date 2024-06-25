# Aqui van los imports

# Menu de opciones para la aplicacion
## El usuario debe ingresar un numero de las opciones valida
def mostrar_menu():
    print("\n######Agenda Telefónica####")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los personas")
    print("4. Salir de la aplicación")
    opcion = int(input("\nIngresa una opción del menu: "))
    return opcion


def agregar_contacto(agenda, nombre, telefono):
    # Diccionario
    agenda[nombre] = telefono
    return f"\nContacto agregado con exito"


def buscar_contacto(agenda, nombre):
    # TODO: Que el return al encontrar contacto muestre su nombre
    if nombre in agenda:
        return f"\nTelefono: {agenda[nombre]}"

    return "\nContacto no encontrado"


# Aqui va la logica del programa
# Se deben integrar todas las funciones que haya
def main():
    pass


if __name__ == "__main__":
    main()
