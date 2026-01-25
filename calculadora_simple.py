print("Hola, bienvenido a la calculadora simple.")

operacion = input("¿Qué operación quieres hacer? (+, -, *, /): ").strip()

if operacion not in {"+", "-", "*", "/"}:
    print("Tu símbolo es inválido.")
    raise SystemExit(1)

print("Ahora ingresa tus números")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
else:  # "/"
    if num2 == 0:
        print("No se puede dividir entre 0.")
        raise SystemExit(1)
    resultado = num1 / num2

print(f"Tu respuesta es: {resultado}")
