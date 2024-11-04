def contar_digitos(titulo):
    contador = 0

    for c in titulo:
        if c.isdigit():
            contador += 1

    return contador


def procesar_linea():
    total_digitos = 0
    bandera = True

    while bandera:
        libro = input("Libro: ")
        if libro == "/":
            bandera = False  
        total_digitos += contar_digitos(libro)
    
    return total_digitos


def main():
    line_count = 0
    bandera = True  

    while bandera:
        total_digitos = procesar_linea()

        if total_digitos is None:
            bandera = False  

        line_count += 1

        print(f"Línea completa. Aparecen {total_digitos} dígitos numéricos.")
    
    print(f"Fin. Se leyeron {line_count} líneas completas.")

if __name__ == "__main__":
    main()
