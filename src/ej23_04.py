def solicitar_numero_entero():
    bandera = True
    while bandera:
        try:
            numero = int(input("Introduce un numero entero: "))

            if numero == 0:
                bandera = False

            print(f"Has introducido el numero entero: {numero}")

        except ValueError:
            print("La entrada no es correcta")

def main():
    solicitar_numero_entero()
if __name__ == "__main__":
    main()
