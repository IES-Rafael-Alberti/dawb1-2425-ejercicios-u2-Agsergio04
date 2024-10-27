def obtener_frase():
    return input("Ingrese una frase: ")


def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras), palabras


def encontrar_palabra_mas_larga(palabras):
    palabra_mas_larga = ""

    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga

def main():
    bandera = True
    while bandera:
        try:
            frase = obtener_frase()

            if not frase.strip():  
                raise ValueError("La frase no puede estar vacia.")
            
            cantidad_palabras, palabras = contar_palabras(frase)
            palabra_mas_larga = encontrar_palabra_mas_larga(palabras)

            
            print(f"La palabra mas larga es: '{palabra_mas_larga}'")
            print(f"Cantidad de palabras: {cantidad_palabras}")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
