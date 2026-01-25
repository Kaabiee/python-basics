import random


print("hola, este es un juego de adivinar un numero aleatorio del 1 al 100.")
respuesta = input("¿Quieres jugar?, contesta con si/no: ")

if respuesta == "si":
    print("Okey, ¡comencemos!")

elif respuesta == "no":
    print("Okey, hasta la proxima.")
    exit()

else:
    print("Respuesta no valida")
    exit()


numero_aleatorio = random.randint(1, 100)

intentos = 0

while True:
    try:
        intento = int(input("Cual crees que es el numero: "))
    except ValueError:
        print("Eso no es un numero valido")
        continue

    intentos += 1

    if intento < numero_aleatorio: 
        print("Te falta.")

    elif intento > numero_aleatorio:
        print("Te pasaste.")

    elif intento == numero_aleatorio:
        print(f"¡Correcto!, lo lograste en {intentos} intentos")
        break
