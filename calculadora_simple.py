print("Hola, bienvenido a la calculadora simple.")
operacion = input("¿Que operacion quieres hacer?, Ingresa tu respuesta con +, -, *,/ : ")
print("Ahora ingresa tus numeros")

if operacion == "+":
    print("Ahora ingresa tus numeros")

elif operacion == "-":
    print("Ahora ingresa tus numeros")
   
elif operacion == "*":
    print("Ahora ingresa tus numeros")
   
elif operacion == "/":
    print("Ahora ingresa tus numeros")
 
else:
    print("Tu simbolo es invalido")

num1 = float(input("Pirimer numero: "))
num2 = float(input("Segundo numero: "))

if operacion == "+":
    suma = num1 + num2 
    print(f"Tu respuesta es: {suma}")

elif operacion == "-":
    rest = num1 - num2
    print(f"Tu respuesta es: {rest}")

elif operacion == "*":
    mult = num1 * num2
    print(f"Tu respuesta es: {mult}")

elif operacion == "/":
    div = num1 / num2
    print(f"Tu respuesta es: {div}")

else:
    print("Tu operacion es invalida.")
