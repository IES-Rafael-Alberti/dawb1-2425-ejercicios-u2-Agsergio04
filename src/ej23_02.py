def pedir_numero():
    return input("Introduce tu numero: ")


def comprobar_numero(numero):
    valor = None

    try:
        valor = int(numero)
        if valor < 0:
            raise ValueError("**ERROR**\nEl numero no puede ser negativa.")
        
    except ValueError:
        print("**ERROR**\nIntroduce una numero valida.")

    return valor  


def cadena_numero(numero):
    linea = " "

    for i in range(1, numero,2):
        linea += str(i) + ","

    linea += str(numero) 

    return linea


def main():
    entrada = pedir_numero()
    valor = comprobar_numero(entrada)

    while valor is None:  
        entrada = pedir_numero()
        valor = comprobar_numero(entrada)

    cadena = cadena_numero(valor)
    print(f"La cadena de 1 hasta {valor} es: {cadena}")

if __name__ == "__main__":
    main()
