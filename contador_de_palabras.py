funciones = """
1.-Contar palabras totales en un texto
2.-Contar caracteres 
3.-Contar oraciones 
4.-Encontrar la palabra más repetida
5.-Mostrar cuántas veces aparece cada palabra 
6.-Contar palabras únicas 
7.-Salir
"""

def contar_palabras(texto):
    palabras = texto.split()
    for index, palabra in enumerate (palabras):
        print(f"Tu texto tiene este numero de palabras: {index + 1}. {palabra}")

def contar_caracteres(texto):
    sin_espacios = texto.replace(" ", "")
    caracteres = len(sin_espacios)
    print(f"Tu texto tiene: {caracteres} Caracteres \n\n\n")

def contar_oraciones(texto):
    oraciones = texto.count(".")
    print(f"Tu texto tiene: {oraciones} Oraciones \n\n\n ")

def encontrar_palabra_mas_repetida(texto):
    lista_palabra = texto.split()
    pmr = {}
    for palabra in lista_palabra:
        palabra = normalizar(palabra)
        if palabra == "":
            continue

        if palabra in pmr:
            pmr[palabra] = pmr[palabra] + 1

        else:
            pmr[palabra] = 1

    # lambda es un def chico(forma de crear funciones pequeñas)
    vlmat = max(pmr.items(), key=lambda kv: kv[1]) if pmr else None
    print(vlmat)

def normalizar(palabra):
    palabra = palabra.strip()
    palabra = palabra.casefold()
    palabra = palabra.strip(".,;:!?¿¡\"'()[]{}")
    return palabra

def mostrar_total_palabra(texto):
    lista_palabra = texto.split()
    pmr = {}

    for palabra in lista_palabra:
        palabra = normalizar(palabra)
        if palabra == "":
            continue

        if palabra in pmr:
            pmr[palabra] += 1
            
        else:
            pmr[palabra] = 1

    print(f"Tu resultado es: {pmr} ")

def contar_palabras_unicas(texto, p):
    p = normalizar(p)
    lista_palabra = texto.split()
    contador = 0

    for palabra in lista_palabra:
        if normalizar(palabra) == p:
            contador += 1

    print(f"La palabra '{p}' aparece {contador} veces en tu texto.\n\n\n")


def salir():
    print("¡Hasta luego!, que tengas un buen dia. ❤️ ")
    exit()

while True:
    try:
        fun = int(input(f"!Hola, bienvenido a el contador de palabras.\nPrimero eligue una opcion {funciones}\nRespuesta: "))

        if fun < 1 or fun > 7:
            print("Tu numero no es valido. ")

        elif fun == 7:
            opcion = int(input("Seguro que quieres salir?\nContesta 1 para continuar o 2 para confirmar que quieres salir.\n\nRespuesta: "))

            try:
                if opcion == 1:
                    print("¡Okey!, continua entonces. ")
                    continue

                elif opcion == 2:
                    print("Entonces si quieres salir. .-.")

                elif opcion < 1 or opcion > 2:
                    print("Tu numero no es valido. ")

            except ValueError:
                print("Esa respusta no es valida. ")

        elif fun == 6:
            texto = input("Ahora pon el texto que quieres utilizar.\n\nTexto: ")
            p = input("¿Cual es la palabra especifica que quieres ver?.\nRespuesta: ")

        else:
            texto = input("Ahora pon el texto que quieres utilizar.\n\nTexto: ")

    except ValueError:
        print("Tu respuesta no es valida. ")

    if fun == 1:
        contar_palabras(texto)

    elif fun == 2:
        contar_caracteres(texto)

    elif fun == 3:
        contar_oraciones(texto)

    elif fun == 4:
        encontrar_palabra_mas_repetida(texto)

    elif fun == 5:
        mostrar_total_palabra(texto)

    elif fun == 6:
        contar_palabras_unicas(texto, p)

    elif fun == 7:
        salir()