menu = """
1.-kilometros a metros
2.-Metros a centimetros
3.-Celsius a Fahrenheit
4.-Salir
"""



while True:
    print("Hola, bienvenido al conversor")
    print(menu)
    opcion = int(input("Selecciona una opcion eliguiendo con numeros 1,2,3 y 4\nResponde:"))

    if opcion == 4:
        print("Hasta luego, cerrando programa...")
        exit()

    elif opcion == 1:
        print("Muy bien, haz eleguido el convertidor de metros a kilometros")
        num1 = float(input("Cuantos kilometros tienes?\nResponde: "))

        num2 = num1 * 1000 
        print(f"tus kilometros son {num2}")


    elif opcion == 2:
        print("Muy bien, haz eleguido el convertidor de Metros a centimetros")
        num1 = float(input("Cuantos Centimetros tienes?\nResponde: "))

        num2 = num1 * 100 
        print(f"tus Centimetros son {num2}")

    elif opcion == 3:
        print("Muy bien, haz eleguido el convertidor de Celsius a Fahrenheit")
        num1 = float(input("Cuantos Celsius tienes?\nResponde: "))

        num2 = (num1 * 1.8) + 32
        print(f"tus Fahrenheit son {num2}")