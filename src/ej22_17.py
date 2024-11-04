def leer_numero():
    return int(input("Introduce un numero(pon 0 para salir): \n"))


def suma_numero(numero):
    suma = 0

    for valor in str(numero):
        suma += int(valor)
    
    return suma


def main():
    numero = " "

    while numero != 0:
        try:
            numero = leer_numero()
            suma = suma_numero(numero)

            print(f"La suma de los valores de {numero} es: {suma}")

        except ValueError:
            print("**ERROR**\nIntroduce solo numeros enteros.")

    

if __name__ == "__main__":
    main()