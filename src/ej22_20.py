def pedir_frase():
    return input("Introduce una frase: ")


def comprobar_letra(letra):
    if len(letra) != 1 or letra.isdigit():

        raise ValueError("Debes introducir solo una letra, no un número.")
    
    return letra


def pedir_letra():
    letra = input("Introduce una letra: ")

    return comprobar_letra(letra)

def buscar_letra(frase, letra):
    for i, caracter in enumerate(frase):  
        if caracter == letra:
            print(f"La letra '{letra}' se encontró en la posición {i}.")
            break

        else:
            print(f"No hay coincidencia en la posición {i}.")

    print(f"La letra '{letra}' no se encontró en la frase.")

def main():
    bandera = True
    
    while bandera:
        try:
            frase = pedir_frase()  
            letra = pedir_letra()   

            buscar_letra(frase, letra)  

        except ValueError as msj:
            print(f"**ERROR**\n{msj}")

if __name__ == "__main__":
    main()
