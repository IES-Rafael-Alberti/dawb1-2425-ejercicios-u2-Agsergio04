def mostrar_palabra_por_palabra(palabra):
    for letra in palabra:
        print(letra)


def pedir_palabra():
    return input("Introduce una palabra: ")


def main():
    bandera = True

    while bandera:
        try:
            palabra = pedir_palabra()

            if palabra.isdigit():
                raise ValueError("No escribasa solo un numero porfavor.")
            
            mostrar_palabra_por_palabra(palabra)

        except ValueError as msj:
            print(f"**ERROR**\n{msj}")
        
if __name__ == "__main__":
    main()