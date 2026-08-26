fun = """
1.-sumar
2.-restar
3.-multiplicar
4.-dividir
5.-salir
"""
e = "tu respuesta no es valida."

def suma(a, b):
    sum = a + b
    print(sum) 
    return sum

def resta(a, b):
    res = a - b
    print(res)
    return res

def multiplicacion(a, b):
    mul = a * b
    print(mul)
    return mul

def division(a, b):
    div = a / b
    print(div)
    return div

def salir():
    print("!Hasta luego que tengas un buen dia¡")
    exit()

while True:
    try:
        res = int(input(f"¿Cual de estas opciones quieres elegir?\n{fun}\nRecuerda que solo puedes contestar con numeros.\nRespuesta:"))

        if res < 1 or res > 5:
            print(f"{e}\n")

        elif res == 5:
            r = int(input("¿Estas seguro que quieres salir?\nPara continuar 1 y para salir 2\nRespuesta: "))

            if r == 1:
                print("Que bueno que quieras continuar. ")
                continue

            elif r == 2:
                print("!Una pena¡")

            if r < 1 or r >2:
                print(f"{e}\n")

            else:
                print(f"{e}\n")

        else:
            a = int(input("¿Cual es tu primer numero?\nRespuesta: "))
            b = int(input("¿Cual es tu segundo numero?\nRespuesta: "))

    except ValueError:
        print(f"{e}\n")

    if res == 1:
        suma(a, b)

    elif res == 2:
        resta(a, b)

    elif res == 3:
        multiplicacion(a, b)

    elif res == 4:
        division(a, b)

    elif res == 5:
        salir()

    else:
        print(f"{e}\n")
        continue