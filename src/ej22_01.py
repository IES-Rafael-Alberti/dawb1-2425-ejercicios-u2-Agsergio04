def repetir_palabra(palabra):
    frase = " "

    for _ in range(10):
        frase += palabra + " "

    return frase


def pedir_usuario():
    return input("Introduce una cadena: ")


def main():
    palabra = pedir_usuario()
    print(repetir_palabra(palabra))


if __name__ == "__main__":
    main()