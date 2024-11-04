def leer_numero():
    return int(input("Introduce un numero(pon 0 para salir): \n"))


def main():
    numero = " "
    numero_mayor = 0

    while numero != 0:
        try:
            numero = leer_numero()
            if numero > 0:
                if numero_mayor < numero:
                    numero_mayor = numero

        except ValueError:
            print("**ERROR**\nIntroduce solo numeros enteros.")

    print(f"El numero mayor positivo introducido es: {numero}")

if __name__ == "__main__":
    main()