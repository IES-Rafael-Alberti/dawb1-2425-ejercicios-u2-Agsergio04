def pedir_frase():
    return input("Introduce una frase: ")


def comprobar_letra(letra):
    
    if len(letra) != 1 or letra.isdigit():
        raise ValueError("Debes introducir solo una letra, no un numero.")
    
    return letra


def pedir_letra():
    letra = input("Introduce una letra: ")
    return comprobar_letra(letra)


def contar_letra(frase, letra):
    return frase.count(letra)


def main():
    bandera = True

    while bandera:
        try:
            frase = pedir_frase()  
            letra = pedir_letra()   

            cantidad = contar_letra(frase, letra)  
            print(f"La letra '{letra}' aparece {cantidad} veces en la frase.")

        except ValueError as msj:
            print(f"**ERROR**\n{msj}")

if __name__ == "__main__":
    main()
