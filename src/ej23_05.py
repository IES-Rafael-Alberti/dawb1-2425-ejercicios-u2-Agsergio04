def pedir_contraseña():
    return input("Introduce la contraseña: ")


def comprobar_contrasenia(contrasenia, pregunta):
    if contrasenia != pregunta:
        raise NameError("Incorrect Password!!")


def main():
    contrasenia = "python"
    bandera = True
    
    while bandera:
        try:
            pregunta = pedir_contraseña().lower()
            comprobar_contrasenia(contrasenia, pregunta)
            bandera = False 
        except NameError as e:
            print(e)

    print("Has iniciado sesión correctamente")

if __name__ == "__main__":
    main()
