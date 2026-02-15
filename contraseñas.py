import string
import random

opciones = """
1.-Generador de contraseña
2.-Verificador de seguridad
3.-Generar mas de una contraseña
4.-Salir
"""

def contraseña():
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    palabra = letras + numeros + simbolos
    d1 = random.choice(palabra)
    d2 = random.choice(palabra)
    d3 = random.choice(palabra)
    d4 = random.choice(palabra)
    d5 = random.choice(palabra)
    d6 = random.choice(palabra)
    d7 = random.choice(palabra)
    d8 = random.choice(palabra)
    d9 = random.choice(palabra)
    d10 = random.choice(palabra)
    d11 = random.choice(palabra)
    d12 = random.choice(palabra)

    contraseña = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12
    return contraseña
    

def generador_de_contraseña():
    print(f"=== Tu contraseña ===\n{contraseña()}")

def verificador_contraseña(tc):
    hay_numero = any(c.isdigit() for c in tc)
    hay_letra = any(c.isalpha() for c in tc)

    if hay_numero and hay_letra:
        print("Tu contraseña es segura. ")

    elif not hay_numero and not hay_letra:
        print("Tu contraseña no tiene numeros ni letras asi que puede no ser segurañ. ")

    elif not hay_letra:
        print("Tu contraseña no tiene letras. ")

    else:
        print("Tu contraseña no tiene numeros. ")

def generador_de_varias_contraseñas(numerodc):
    if numerodc < 1 or numerodc > 10:
        print("Tu numero no es valido. Solo se pueden generar de 1 a 10.")
        return

    for i in range(numerodc):
        print(f"{i + 1}.- {contraseña()}")

def salir():
    exit()

while True:
    try:
        r = int(input(f"¿Que opcion quieres utilizar?\n{opciones}\nRespuesta:"))

        if r == 4:
            res = int(input("¿Seguro que quieres salir?\n1 para salir y 2 para continuar.\nRespuesta: "))

            if res == 1:
                print("¡Okey!, que tengas un buen dia. ")
                exit()
            
            elif res == 2:
                print("¡Que bueno que quieras continuar! ")
                break

            else:
                print("Tu respuesta no es valida.")
                continue

        if r < 1 or r > 4:
            print("Tu respuesta no es valida. Intentalo de nuevo. ")
            continue

        elif r == 3:
            numerodc = int(input("¿Cuantas contraseñas quieres generar?\nSolo se pueden generar 10 y tu respuesta tiene que ser con numeros.\nRespuesta: "))

            if numerodc < 1 or numerodc > 10:
                print("Tu numero no es valido. ")
                continue

            else:
                print("=== Tus contraseñas ===")

        elif r == 2:
            tc = input("Escribe tu contraseña: ")
                
        
    except ValueError:
        print("Tu respuesta no es valida. ")

    if r == 1:
        generador_de_contraseña()

    elif r == 2:
        verificador_contraseña(tc)

    elif r == 3:
        generador_de_varias_contraseñas(numerodc)

    elif r == 4:
        salir()

    else:
        print("Tu respuesta no es valida. ")
