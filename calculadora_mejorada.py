import math

resultados = []

opciones = """
1.-Suma
2.-Resta
3.-Multiplicación
4.-División
5.-Potencia
6.-Raiz cuadrada
7.-Porcentaje
8.-Modulo
9.-Ver Historial
10.-Limpiar historial
11.-Salir
"""

def guardar_operaciones():
    with open("operaciones.txt", "w") as archivo:
        archivo.write("OPERACIONES\n")
        for resultado in resultados:
            archivo.write(resultado + "\n")

def cargar_operaciones():
    try:
        with open("operaciones.txt", "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                linea = linea.strip()

                if linea == "OPERACIONES" or linea == "":
                    continue

                resultados.append(linea)

    except FileNotFoundError:
        pass

def suma():
    print("¡Genial!, Elegiste suma. ")
    resultado = num1 + num2
    print(f" Tu respuesta es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} + {num2} = {resultado}")
    guardar_operaciones()

def resta():
    print("¡Genial!, Elegiste resta. ")
    resultado = num1 - num2
    print(f"Tu respuesta es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} - {num2} = {resultado}")
    guardar_operaciones()

def multiplicacion():
    print("¡Genial!, Elegiste multiplicacion. ")
    resultado = num1 * num2
    print(f"Tu respuesta es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} * {num2} = {resultado}")
    guardar_operaciones()

def division():
    print("¡Genial!, Elegiste division. ")
    resultado = num1 / num2 
    print(f"Tu resultado es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} / {num2} = {resultado}")
    guardar_operaciones()

def potencia():
    print("¡Genial!, Elegiste potencia. ")
    resultado = math.pow(num1, num2)
    print(f"Tu resultado es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} ^ {num2} = {resultado}")
    guardar_operaciones()

def raiz_cuadrada():
    print("¡Genial!, Elegiste raiz cuadrada. ")
    resultado = math.sqrt(num1)
    print(f"Tu resultado es: {resultado} \n\n\n\n")
    resultados.append(f"√{num1} = {resultado}")
    guardar_operaciones()

def porcentaje():
    print("¡Genial!, Elegiste porcentaje. ")
    num3 = 100
    resultado = num1 * num2 / num3
    print(f"Tu resultado es: {resultado} \n\n\n\n")
    resultados.append(f"{num1} * {num2} / {num3} = {resultado}")
    guardar_operaciones()

def modulo():
    print("¡Genial!, Elegiste modulo")
    resultado = num1 % num2
    print(f"Tu resultado es : {resultado} \n\n\n\n")
    resultados.append(f"{num1} % {num2} = {resultado}")
    guardar_operaciones()

def ver_historial():
    print("¡Genial!, Elegiste ver historial. ")
    print("===== Tu historial =====\n\n\n\n")
    for resultado in resultados:
        print(resultado, "\n\n\n\n")

def limpiar_historial():
    print("¡Genial!, Elegiste limpiar historial. ")
    print("===== Tu historial ha sido borrado =====\n\n\n\n")
    resultados.clear()
    guardar_operaciones()

def salir():
    exit()

cargar_operaciones()

print("!Hola, Buen dia¡. ")

while True:
    try:
        respuesta = int(input(f"¿Que operacion deseas hacer el dia de hoy?.\nContesta solo con 1,2,3...\n{opciones}\nRespuesta: "))
        
        if respuesta < 1 or respuesta > 11:
            print("Tu numero no es valido, por favor intenta de nuevo. ")

        elif respuesta == 6:
            num1 = int(input("¿De que numero quieres sacar su raiz cuadrada?\nRecuerda que no se puede usar el valor 0\nRespuesta:"))

            if num1 == 0:
                print("Tu numero no es valido. ")
                continue

            else:
                print("Tu numero fue agregado con exito. ")

        elif respuesta == 9:
            resp1 = input("Quieres ver tu historial?\nResponde con si/no\nRespuesta: ")
            
            if resp1 == "no":
                continue
            
            elif resp1 == "si":
                print("====== Tu historial ======")

            else:
                print("Tu respuesta no es valida. ")
                continue

        elif respuesta == 10:
            resp1 = input("Estas seguro de querer borrar tu historia?\nResponde con si/no\nRespuesta: ")

            if resp1 == "no":
                print("Okey, tu historial no sera borrado. ")
                continue
            
            elif resp1 == "si":
                print("Tu historial ha sido borrado con exito. ")

            else:
                print("Tu respuesta no es valida. ")
                continue

        elif respuesta == 11:
            resp1 = input("¿Estas seguro de que quieres salir?\nContesta con un si/no\nRespuesta: ")

            if resp1 == "no":
                print("Okey, Entonces no vas a regresar al menu. ")
                continue

            elif resp1 == "si":
                print("¡Hasta luego!, que tengas un buen dia. ")
            

            else:
                print("TU respuesta no es valida. ")
                continue
            
        else:
            num1 = int(input("¿Cual es el primer numero?\nRecuerda que no se puede usar el valor 0\nRespuesta: "))
            
            if num1 == 0:
                print("Tu numero no es Valido. ")
                continue
            
            else:
                print("Numero agregado con exito. ")

            num2 = int(input("¿Cual es el segundo numero?: "))

            if num2 == 0:
                print("Tu numero no  es Valido. ")
                continue

            else:
                print("Numero agregado con exito. ")

    except ValueError:
        print("Ese no es un numero valido. ")
        continue

    if respuesta == 1:
        suma()

    elif respuesta == 2:
        resta()

    elif respuesta == 3:
        multiplicacion()

    elif respuesta == 4:
        division()

    elif respuesta == 5:
        potencia()

    elif respuesta == 6:
        raiz_cuadrada()

    elif respuesta == 7:
        porcentaje()

    elif respuesta == 8:
        modulo()

    elif respuesta == 9:
        ver_historial()

    elif respuesta == 10:
        limpiar_historial()

    elif respuesta == 11:
        salir()

    else:
        print("Esa no es una respuesta Valida: ")
        continue