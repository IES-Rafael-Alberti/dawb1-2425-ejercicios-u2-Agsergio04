def leer_numero():
    return int(input("Introduce un numero(pon 0 para salir): \n"))


def main():
    numero = " "
    suma = 0

    while numero != 0:
        try:
            numero = leer_numero()
            if numero > 0:
                suma  += numero

        except ValueError:
            print("**ERROR**\nIntroduce solo numeros enteros.")

    print(f"La suma de los numeros es: {suma}")

if __name__ == "__main__":
    main()