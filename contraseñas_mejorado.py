import string 
import random 

fun = """
1.-Generador de contraseñas
2.-Calcular fuerza de contraseña
3.-Generador de varias contraseñas
4.-Generador de contraseña memorable
5.-Generar contraseña personalizada 
6.-Ver historial de contraseñas generadas
7.-Guardar contraseñas en un archivo.txt
8.-Generar pin numerico
9.-Salir
"""

er = "Tu respuesta no es valida.\n\n\n"

def contraseña():
    pool = string.ascii_letters + string.punctuation + string.digits

    caracteres = []
    for i in range (15):
        letra = random.choice(pool)
        caracteres.append(letra)

    print(''. join(caracteres))


def seguridad():
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tienfe_minuscula = any(c.islower() for c in contraseña)
    tiene_simbolo = any(c in string.punctuation for c in contraseña)
    hay_numero = any(c.isdigit() for c in contraseña)
    hay_letra = any(c.isalpha() for c in contraseña)
    longitud_ok = len(contraseña) >= 8


TENGO QUE HACER LOS IFS DE ESTA FUNCION.



    if hay_numero and hay_letra:
        print("Tu contraseña es segura. ")

    elif not hay_numero and not hay_letra:
        print("Tu contraseña no tiene numeros ni letras asi que puede no ser segurañ. ")

    elif not hay_letra:
        print("Tu contraseña no tiene letras. ")

    else:
        print("Tu contraseña no tiene numeros. ")






def varias_contraseñas(num):
    print("====== Tus contraseñas ======\n\n\n")
    
    for i in range(num):
        print(f"{i+1}.- {contraseña()}")

def salir():
    print("Que tengas un buen dia, !Hasta luego¡👋🏻")
    exit()

while True:
    try:
        txt = int(input(f"¿Cual opciones quieres utilizar?\n{fun}\nRecuerda que solo puedes responder con numeros.\nRespuesta: "))
        print("\n")
        
        if txt == 1:
                    print("====== Tu contraseña ======\n\n\n")
        
        elif txt == 2:
            contraseña = input("Por favor escribe tu contraseña.\nContraseña: ")

        elif txt == 3:
            num = int(input("¿Cuantas contraseñas quieres generar?\nRecuerda que el maximo son 20 contraseñas.\nNumero de contraseñas: "))

            if num < 1 or num > 20:
                print(er)
                continue

        elif txt == 4:
            print("====== Tu contraseña memorable ======")

        if txt < 1 or txt > 9:
            print(er)

    except ValueError:
        print(er)
        continue

    if txt == 1:
        contraseña()

    elif txt == 2:
        seguridad()

    elif txt == 3:
        varias_contraseñas(num)

    elif txt == 9:
        salir()

    else:
        print(er)