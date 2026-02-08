opciones = """
1.-Consultar saldo
2.-Depositar dinero
3.-Retirar dinero
4.-Ver historial de transacciones
5.-salir
"""

depositos = """
1.-Tu cuenta
2.-Otra cuenta
"""
saldo = []
depositose = []

def consultar_saldo():
    total = sum(saldo)
    if total == 0:
        print("Aun no tienes saldo. Por favor haz un deposito ")

    else:
        print("====== Tu saldo es ====== ")
        print(total)
        print("\n\n\n\n")

def depositar_dinero():
    while True:
        print("¿A quien le quieres depositar dinero?")
        print(depositos)
        res = int(input("Recuerda contestar solo con numeros\nRespuesta: "))

        if res == 1:
            monto = float(input("¿Cuanto es el monto te quieres depositar?\nMonto: "))

            if monto < 1:
                print("No puedes poner cantidades negativas. ")

            else:
                print(f"Tu deposito de {monto} a sido completado con exito.\n\n\n\n ")
                saldo.append(monto)
                break

        elif res == 2:
            persona = input("¿A quien le quieres depositar?\nEscribe el nombre. ").upper()
            monto = float(input(f"¿Cuanto es el monto que quieres depositar a {persona}. "))
            
            if monto < 1:
                print("No puedes poner cantidades negativas. ")

            else:
                print(f"Su deposito se completo con exito a {persona} ")
                depositose.append( (persona, monto) )
                break

        else:
            print("Tu respuesta no es valida")
            continue

def retirar_dinero():
    try:
        res = float(input("¿Cuanto dinero quieres retirar?\nMonto que se quiere retirar: "))
    except ValueError:
        print("Tu respuesta no es valida")
        return

    if res <= 0:
        print("El monto debe ser mayor que 0. ")
        return

    if res > sum(saldo):
        print("No tienes saldo suficiente para retirar esta cantidad. ")
    else:
        print("Tu retiro se ha completado con exito. ")
        saldo.append(-res)
        

def ver_historial():
    print("====== Tu historial ====== ")
    for monto in saldo:
        print(monto)

    print("====== Personas a las que haz hecho transacciones ======")
    for persona, monto in depositose:
        print(persona, monto)

def salir():
    print("¡Hasta Luego!, que tengas un buen dia❤️")
    exit()

while True:
    try:
        print("====== Cajero Automatico. ====== ")
        print("Las opciones son:")
        print(opciones)
        respuesta = int(input("Que opcion eligues?, usa numeros para responder. "))

        if respuesta < 1 or respuesta > 5:
            print("Tu numero no es valido. ")
            continue

        else:
            print(f"Eleguiste la opcion numero {respuesta}. ")
        
    except ValueError:
        print("Tu respuesta no es valida")
        continue


    if respuesta == 1:
        consultar_saldo()

    elif respuesta == 2:
        depositar_dinero()    

    elif respuesta == 3:
        retirar_dinero()

    elif respuesta == 4:
        ver_historial()

    elif respuesta == 5:
        salir()

    else:
        print("Tu respuesta no es valida. ")
