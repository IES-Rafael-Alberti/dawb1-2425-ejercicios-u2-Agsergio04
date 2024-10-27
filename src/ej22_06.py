def crear_triangulo(altura):
    linea = " "

    for valor in range(altura + 1):
        linea += "*" * valor + "\n"
        

    return linea


def pedir_usuario():
     return int(input("Introduce la altura del triangulo: "))


def main():
    bandera = True

    while bandera:
            try:
                altura = pedir_usuario() 
                triangulo = crear_triangulo(altura)

            except ValueError:
                print("**ERROR**\nIntroduce un parametro valido.")
            else:
                print(triangulo)

if __name__ == "__main__":
    main()