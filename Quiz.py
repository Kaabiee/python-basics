aciertos = []
fallos = []

_1 = {
    "pregunta": "¿Quién escribió Don Quijote de la Mancha?",
    "opciones": ["Gabriel García Márquez", "Miguel de Cervantes", "William Shakespeare"],
    "respuesta_correcta": "Miguel de Cervantes"

}
    
_2 = {
    "pregunta": "¿Cuál es el elemento químico representado por el símbolo Au?",
    "opciones": ["Plata", "Oro", "Aluminio"],
    "respuesta_corecta": "Oro"
}

_3 = {
    "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
    "opciones": ["Saturno", "Júpiter", "Neptuno"],
    "respuesta_correcta": "Júpiter"
}

_4 = {
    "pregunta": "¿En qué año llegó el hombre a la Luna?",
    "opciones": ["1969", "1959", "1979"],
    "respuesta_correcta": "1969"
}

_5 = {
    "pregunta": "¿Cuál es el océano más grande del mundo?",
    "opciones": ["Atlántico", "Índico", "Pacífico"],
    "respuesta_correcta": "Pacífico"
}

_6 = {
    "pregunta": "¿Quién pintó la Mona Lisa?",
    "opciones": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso"],
    "respuesta_correcta": "Leonardo da Vinci"
}

_7 = {
    "pregunta": "¿Cuál es la capital de Francia?",
    "opciones": ["Londres", "Berlín", "París"],
    "respuesta_correcta": "París"
}

_8 = {
    "pregunta": "¿Qué gas respiramos principalmente del aire?",
    "opciones": ["Oxígeno", "Nitrógeno", "Dióxido de carbono"],
    "respuesta_correcta": "Nitrógeno"
}

_9 = {
    "pregunta": "¿Cuántos continentes hay en el mundo?",
    "opciones": ["5", "6", "7"],
    "respuesta_correcta": "7"
}

_10 = {
    "pregunta": "¿Cuál es el animal terrestre más rápido?",
    "opciones": ["León", "Guepardo", "Caballo"],
    "respuesta_correcta": "Guepardo"
}

def pregunta_1():
    while True:
        print(_1["pregunta"])
        print(_1["opciones"])
        res = input("¿Cual es la opcion que eliges?\nRespuesta: ")
    
        if res == "miguel de cervantes":
            print("Tu respuesta es correcta. \n\n\n\n\n")
            aciertos.append(res)
            break

        elif res == "gabriel garcia marquez":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_1['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "william shakespeare":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_1['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)

            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_2():
    while True:
        print(_2["pregunta"])
        print(_2["opciones"])
        res = input("¿Cual es la opcion que eliges?\nRespuesta: ")

        if res == "oro":
            print("Tu respuesta es la correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "plata":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_2['respuesta_corecta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "aluminio":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_2['respuesta_corecta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_3():
    while True:
        print(_3["pregunta"])
        print(_3["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "jupiter":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "saturno":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_3['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "neptuno":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_3['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_4():
    while True:
        print(_4["pregunta"])
        print(_4["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "1969":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "1959":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_4['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "1979":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_4['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_5():
    while True:
        print(_5["pregunta"])
        print(_5["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "pacifico":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "indico":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_5['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "atlantico":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_5['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_6():
    while True:
        print(_6["pregunta"])
        print(_6["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "leonardo da vinci":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "pablo picasso":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_6['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "vicent van gogh":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_6['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_7():
    while True:
        print(_7["pregunta"])
        print(_7["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "paris":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "berlin":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_7['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "londres":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_7['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_8():
    while True:
        print(_8["pregunta"])
        print(_8["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "nitrogeno":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "oxigeno":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_8['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "dioxido de carbono":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_8['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_9():
    while True:
        print(_9["pregunta"])
        print(_9["opciones"])
        res = int(input("¿Cual es la opcion que eliges\nRespuesta: "))

        if res == 7:
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == 5:
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_9['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == 6:
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_9['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

def pregunta_10():
    while True:
        print(_10["pregunta"])
        print(_10["opciones"])
        res = input("¿Cual es la opcion que eliges\nRespuesta: ")

        if res == "guepardo":
            print("Tu respuesta es correcta.\n\n\n\n\n ")
            aciertos.append(res)
            break

        elif res == "leon":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_10['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        elif res == "caballo":
            print("Te equivocaste. ")
            print(f"La respuesta correcta es: {_10['respuesta_correcta']}\n\n\n\n\n")
            fallos.append(res)
            break

        else:
            print("Tu respuesta no es valida.\n\n\n\n\n ")

while True:
    try:
        respuesta = input("¡Hola!, bienvenido a este Quiz de preguntas generales.\n¿Quieres participar en este?\nTu respuesta que sea un si/no. ")
        if respuesta == "no":
            print("Okey, que tengas un buen dia. ")
            break

        elif respuesta == "si":
            print("¡Ya veo que quieres probar tus conocimientos!\n\n")

        else:
            print("Tu respuesta no es valida.\n ")

    except ValueError:
        print("Tu respuesta no es valida. ")
        continue

    print("Comencemos con la primera pregunta. ")
    pregunta_1()

    print("Ahora la Siguiente pregunta. ")
    pregunta_2()

    print("Siguiente pregunta. ")
    pregunta_3()

    print("Siguiente pregunta. ")
    pregunta_4()

    print("Siguiente pregunta. ")
    pregunta_5()

    print("Siguiente pregunta. ")
    pregunta_6()

    print("Siguiente pregunta. ")
    pregunta_7()

    print("Siguiente pregunta. ")
    pregunta_8()

    print("Siguiente pregunta. ")
    pregunta_9()

    print("Ultima pregunta. ")
    pregunta_10()

    if aciertos:
        print("=====¡Felicidades, tus aciertos son: ===== \n")
        for index, acierto in enumerate (aciertos):
            print(f"{index + 1}. {acierto}\n")
        
    else:
        print("===== No tuviste ningun acierto. =====\n ")


    if fallos:
        print("=====Tus fallos son: =====\n ")
        for index, fallo in enumerate (fallos):
            print(f"{index + 1}. {fallo}\n")

    else:
        print("===== Felicidades no tuviste ningun fallo. =====\n ")

    exit()




    
    