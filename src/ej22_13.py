def pedir_entrada():
    return input("Introduce algo (escribe 'salir' para terminar): ")


def mostrar_ecos():
    bandera = True
    while bandera:
        entrada = pedir_entrada()  

        if entrada.lower() == "salir":  
            print("Programa terminado.")
            bandera = False

    print(f"Eco: {entrada}")  

def main():
    mostrar_ecos()  

if __name__ == "__main__":
    main()
