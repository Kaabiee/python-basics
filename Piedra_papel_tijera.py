import random

print("hola, bienvenido.")
iniciar = input("¿Quieres jugar piedra, papel o tijera contra Pablo?, contesta con s/n: ")

if iniciar == "s":
    print("Okey, !empecemos¡")

elif iniciar == "n":
    print("Hasta luego, !Que tengas un buen dia¡.")
    exit()

else:
    print("Tu respuesta es incorrecta, Por favor intentalo de nuevo.")
    exit()

intentos = 0

while True:
    try:
        me = input("Eligue una opcion piedra, papel, tijera: ")
    except ValueError:
        print("Esa es una opcion no valida.")
        continue

    pab = random.choice(["piedra", "papel", "tijera"])

    intentos += 1

    if me == "piedra":
        if pab == "piedra":
            print("Empate")

        elif pab == "tijera":
            print("!Tu ganas¡, piedra aplasta tijeras.")
            jugar_otra = input("¿Quieres jugar otra ronda?, (S/n): ")
            if jugar_otra == "n":
                break

        elif pab == "papel":
            print("!Tu pierdes¡, el papel le gana a la piedra")
        
    elif me == "tijera":
        if pab == "tijera":
            print("Empate")

        elif pab == "papel":
            print("!Tu ganas¡, las tijeras cortan al papel")
            jugar_otra = input("¿Quieres jugar otra ronda?, (S/n): ")
            if jugar_otra == "n":
                break

        elif pab == "piedra":
            print("!Tu pierdes¡, la piedra destruye a las tijeras")

    elif me == "papel":
        if pab == "papel":
            print("Empate")

        elif pab == "piedra":
            print("!Tu ganas¡, el papel gana a la piedra")
            jugar_otra = input("¿Quieres jugar otra ronda?, (S/n): ")
            if jugar_otra == "n":
                break

        elif pab == "tijera":
            print("!Tu pierdes¡, las tijeras cortan el papel")
        
    else:
        print("Tu mensaje no es valido.")
        continue