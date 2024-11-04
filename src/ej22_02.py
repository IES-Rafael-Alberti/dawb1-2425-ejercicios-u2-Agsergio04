def pedir_edad():
    return input("Introduce tu edad: ")


def comprobar_edad(edad):
    valor = None

    try:
        valor = int(edad)
        if valor < 0:
            raise ValueError("**ERROR**\nLa edad no puede ser negativa.")
        
    except ValueError:
        print("**ERROR**\nIntroduce una edad valida.")

    return valor  


def cadena_edad(edad):
    linea = " "

    for i in range(1, edad + 1):
        linea += str(i) + " "
        
    return linea


def main():
    entrada = pedir_edad()
    anios = comprobar_edad(entrada)

    while anios is None:  
        entrada = pedir_edad()
        anios = comprobar_edad(entrada)

    cadena = cadena_edad(anios)
    print(f"La cadena de 1 hasta {anios} es: {cadena}")

if __name__ == "__main__":
    main()
