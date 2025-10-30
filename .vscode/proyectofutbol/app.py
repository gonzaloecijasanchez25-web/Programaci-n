lista_equipos = []
equipo = {}
nombre = 0
ciudad = 0
estado = 0
seguir = 0
mensaje = ""

from equipos import generar_id, crear_equipo, listar_equipos

def menu_equipo():
    seguir = 0
    while seguir == 0:
        print("-----MENU EQUIPOS-----")
        print("1. Añadir Equipos")
        print("2. Listar Equipos")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                mensaje = crear_equipo(lista_equipos)
                print(mensaje)
            case "2":
                mensaje = listar_equipos(lista_equipos)
                print(mensaje)
            case "6":
                print("Yendo a menu general")
                seguir += 1



menu_equipo()