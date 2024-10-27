def leer_numero():
    return int(input("Introduce un numero(pon -1 para salir): \n"))


def par_o_impar(numero):
    comprobacion = False 

    if (numero % 2 == 0):
        comprobacion = True
    
    return comprobacion
    

def main():
    numero = " "
    contador = 0
    suma = 0

    while numero != -1:
        try:
            numero = leer_numero()
            if numero > 0:
                if par_o_impar(numero):
                    contador += 1
                suma += numero

        except ValueError:
            print("**ERROR**\nIntroduce solo numeros enteros.")

    print(f"La suma de los numeros postivios es {suma} y has introducido un total de {contador} numeros pares.")

if __name__ == "__main__":
    main()