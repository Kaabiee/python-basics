print("hola, bienvenido/a a lista de tareas. ")

tareas_p = []
tareas_t = []

while True:
    objetivo = input("Que deseas hacer?, Contesta con (1,2,3,4,5,6,7,8)\n1.-Agregar una tarea\n2.-Ver tus tareas pendientes\n3.-Eliminar tareas\n4.-Marcar como terminadas\n5.-Editar tareas\n6.-Numero de tareas\n7.-Limpiar tareas\n8.-Salir\nSeleccion: ")
    if objetivo  == "1":
            print("Agregar tarea ")
            tarea = input("Nombre de la tarea: ")
            tareas_p.append(tarea)
            print("Tarea agregada con exito. ")

    elif objetivo == "2":
         print("Tus tareas pendientes. ")
         for tarea in tareas_p: #Te permite ver cada elemento de una lista
              print(tarea)

    elif objetivo == "3":
         print("¿Que tarea deseas eliminar?: ")
         eli = input("¿Nombre de la tarea que deseas eliminar?: ")
         tareas_p.remove(eli)
         print(f"La tarea {eli} a sido eliminada con exito. ")

    elif objetivo == "4":
         ter = input("¿Que tarea deseas marcar como terminada?: ")
         tareas_p.remove(ter)
         tareas_t.append(ter)
         print("Tu tarea a sido marcada como terminada. ")

    elif objetivo == "5": 
        res = input("¿Quieres editar una tarea pendiente o terminada?: ")
        if res == "pendiente":
            print("Tus tareas. ")
            print("=== Tareas Pendientes ===")
            for index, tarea in enumerate(tareas_p):
                print(f"{index + 1}. {tarea}")
            edit = int(input("¿Que tarea quieres editar?, contesta con numeros 1,2,3,etc.: "))
            nombre_nuevo = input("Que nombre quieres poner?: ")
            tareas_p[edit - 1] = nombre_nuevo
        
        elif res == "terminada":
            print("Tus tareas. ")
            print("\n=== Tareas Terminadas ===")
            for index, tarea in enumerate(tareas_t):
                print(f"{index + 1}. {tarea}")
            edit = int(input("¿Que tarea quieres editar?, contesta con numeros 1,2,3,etc.: "))
            nombre_nuevo = input("Que nombre quieres poner?: ")
            tareas_t[edit - 1] = nombre_nuevo

        else:
            print("Tu respuesta no es valida. ")
            continue

    elif objetivo == "6":
        print("Tus tareas son: ")
        for tareas in tareas_p:
            print(tareas)
        for tareas in tareas_t:
            print(tareas)

    elif objetivo == "7":
        res2 = input("¿Quieres eliminar las tareas pendientes?, contesta con (si/no):")
        
        if res2 == "si":
            tareas_t.clear()
            print("Se borraron todas las tareas terminadas. ")

        elif res2 == "no":
            print("Entendido. ")
            continue
        
        else:
            print("Respuesta no valida. ")
            continue

    elif objetivo == "8":
        print("Hasta luego, !Que tengas un buen dia¡")
        exit()

    else:
        print("Tu seleccion es invalida")
        exit()