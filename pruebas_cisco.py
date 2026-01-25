import getpass

def main():
    print("hola, mundo")
    print("esto es una prueba de cisco")    
    print("para comenzar, ¿Cual es tu nombre?")
    nombre = input("nombre: ")
    print(f"Bienvenido/a, {nombre}! Gracias por usar cisco para tu aprendizaje")
    print("Para continuar, necesitas contestar las siguientes preguntas: ")
    nacionalidad = input("nacionalidad: ")
    edad = input("edad: ")
    print("Ahora crea una cuenta con tu correo electronico y una contrasena segura")
    correo_electronico = input("correo electronico: ")
    contrasena = getpass.getpass("contrasena: ")

if __name__ == "__main__":
    main()