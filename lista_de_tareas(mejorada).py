print("!Hola¡, Bienvenido/a a tu lista de tareas. ")

tareas_p = []
tareas_t = []

menu_texto = """
1.-Agregar una tarea
2.-Ver tus tareas pendientes
3.-Eliminar tareas pendientes
4.-Marcar como terminadas
5.-Editar tareas
6.-Numero de tareas
7.-Limpiar tareas terminadas
8.-Salir
"""

# las definiciones me ayudan a poder reutilizarlas en el futuro
def agregar_tarea():
    while True:
        tarea = input("¿Que nombre quieres agregar a la tarea?: ")
        if tarea in tareas_p:
            print("Tu tarea no se puede agregar ya que existe una tarea con el mismo nombre. ")
            continue

        else:
            print("Tu tarea ha sido agregada con exito. ")
            tareas_p.append(tarea)
            break

def ver_tareas_pendientes():
    print("Tus tareas pendientes son: ")
    for tarea in tareas_p:
        print(tarea)

def eliminar_tareas_p():
    print("¿Que tarea deseas eliminar?")
    while True: 
            eli = input("Nombre de la tarea que deseas eliminar: ")
            if eli in tareas_p:
                tareas_p.remove(eli)
                print("Tu tarea a sido eliminada con exito. ")
                break

            elif eli not in tareas_p:
                print("No existe ninguna tarea con ese nombre. ")
                
                salir = input("¿Deseas continuar o salir de este menu?, contesta con continuar o salir.\n respuesta: ")
                    
                if salir == "continuar":
                    continue

                elif salir == "salir":
                    break
                    
                else:
                    print("Tu respuesta no es valida. ")

def marcar_terminada():
    print("¿Que tarea quieres marcar como terminada? ")
    while True:
        try:
            ter = input("Nombre: ")
            if ter in tareas_p:
                tareas_p.remove(ter)
                tareas_t.append(ter)
                print("Tu tarea a sido marcada como terminada. ")
                break

            else:
                print("No existe ningunar tarea pendiente con ese nombre. ")
                continue 

        except ValueError:
            print("No se puedo marcar como terminada tu tarea.")
            exit()

def editar_tarea():
    while True:
        res = input("¿Quieres editar una tarea pendiente o terminada?")
        if res == "pendiente":
            print("Tus tareas. ")
            print("=== Tus tareas pendientes ===")
            for index, tarea in enumerate (tareas_p):
                print(f"{index + 1}. {tarea}")
            edit = int(input("¿que tarea quieres editar?.\nContesta con numeros 1.2.3.4.etc."))
            nombre_nuevo = input("¿Cual es el nuevo nombre que deseas utilizar?. ")
            tareas_p[edit - 1] = nombre_nuevo
            break

        elif res == "terminada":
            print("Tus tareas. ")
            print("=== Tus tareas pendientes ===")
            for index, tarea in enumerate (tareas_t):
                print(f"{index + 1}. {tarea}")
            edit2 = int(input("¿Que tarea quieres editar?.\nContesta con numeros 1.2.3.4.etc.")) 
            nombre_nuevo = input("¿Cual es el nuevo nombre que deseas utilizar. a")
            tareas_t.[edit2 - 1] = nombre_nuevo
            break

        else:
            print("Tu respuesta no es valida. ")
            continue

def numero_de_tareas():
    print("==== Tus tareas pendientes ====")
    for tarea in tareas.p:
        print(tarea)
        
    print ("==== Tus tareas terminadas son ====")
    for tarea in tareas_t:
        print(tarea)

def borrar_tareas_terminadas():
    while True:
    resp3 = input("Estas seguro de que quieres eliminar las tareas terminadas?.\n Contesta con un (si/no);")
        if resp3 == "si":
            tareas_t.remove()
            print("Tus tareas han sido eliminadas con exito. ")
            break

        elif resp3 == "no":
            print("Okey. ")
            break

        else:
            print("Tu respuesta no es valita. vuelve a intentarlo. ")
            continue

def salir():
    print("!Que tengas un buen dia¡, hasta luego.")
    exit()

while True:
    try:
        opciones = int(input(f"¿Que deseas hacer?, selecciona tu respuesta con 1,2,3,4,5,6,7,8\n{menu_texto}Seleccion: "))
        if opciones < 1 or opciones > 8:
            print("Ese numero no esta entre las opciones (1-8)")
        else:
            print(f"!Genial, elegiste: {opciones}")
    except ValueError:
        print("Eso no es un numero valido. ")
        continue
        
    if opciones == 1:
        agregar_tarea()
    
    elif opciones == 2:
        ver_tareas_pendientes()

    elif opciones == 3:
        eliminar_tareas_p()

    elif opciones == 4:
        marcar_terminada()

    elif opciones == 5:
        editar_tarea()

    elif opciones == 6:
        numero_de_tareas()        

    elif opciones == 7:
        borrar_tareas_terminadas()

    elif opciones == 8:
        salir()        

    else:
        print("Tu seleccion fue invalida.\nPor favor intenta de nuevo. ")
        continue
