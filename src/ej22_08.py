def crear_triangulo(altura):
    cadena = ""
    triangulo = ""
    inicio = 1
    
    for i in range(inicio,altura + 1,2):
        cadena = str(i) + " " + cadena
        triangulo = triangulo + cadena + " \n"
    
    return triangulo


def comprobar_numero():
    while True:
        try:
            numero = input("Introduce un número entero positivo: ")
            numero_entero = int(numero)
            
            if numero_entero < 0:
                raise ValueError("Introduce un número entero positivo.")
            
            return numero_entero
        except ValueError as mensaje:
            print(f"**ERROR**\n{mensaje}")

    
def main():
    
    altura = comprobar_numero()
    
    triangulo = crear_triangulo(altura)

    print(triangulo)
    
if __name__ == "__main__":  
    main()
