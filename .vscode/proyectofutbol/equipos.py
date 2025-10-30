    # Modulo 1
    #variables usadas 
lista_equipos = []
equipo = {}
nombre = 0
ciudad = 0
estado = 0
    #definimos funciones
def generar_id(lista_equipos):
        return len(lista_equipos) + 1

def crear_equipo(lista_equipos):
        nombre = input("Introduce el nombre del equipo: ")
        ciudad = input(f"Introdue la ciudad donde se encuentre {nombre}: ")
        Estado = "Inactivo"
        if nombre == "" or ciudad == "":
            print("Ciudad y nombre no pueden estar vacíos")
            return
        
        for equipo in lista_equipos:
            if equipo["nombre"] == nombre:
                print ("Este equipo ya existe")
                return
        
        else:
            Estado = "Activo"

        equipo = {
            "id" : generar_id(lista_equipos),
            "nombre": nombre,
            "ciudad": ciudad,
            "estado": Estado
        }
        lista_equipos.append(equipo)
        return f"{equipo} creado correctamente"


def listar_equipos(lista_equipos):
    if len(lista_equipos) == 0:
        print("No hay equipos, vuelva a la primera opcion para añadir")
        return
    else:
        texto = ""
        for i in lista_equipos:
            estado = "Activo" if i["estado"] == "Activo" else "Inactivo"
            texto += f'ID:{i["id"]} | Equipo:{i["nombre"]} | Ciudad:{i["ciudad"]} | Estado:{estado}\n'
        return texto
    