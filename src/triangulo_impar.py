def crear_triangulo_impar(altura):
    cadena = ""
    triangulo = ""
    
    for i in range(1,altura + 1,2):
        cadena += str(i) + " "
        triangulo += cadena [::-1] + "\n"
    
    return triangulo

def crear_triangulo_par(altura):
    cadena = ""
    triangulo = ""
    
    for i in range(0,altura,2):
        cadena += str(i) + " "
        triangulo += cadena [::-1] + "\n"
    
    return triangulo

def par_o_impar(valor):
    comprobacion = True
    if (valor % 2 == 0):
        comprobacion = False
    
    return comprobacion


def comprobar_numero():
    condicion = True
    
    while condicion:
        try:
            numero = input("Introduce un número entero: ")
            numero_entero = int(numero)
            
            if numero_entero < 0:
                raise ValueError("**ERROR***\nIntroduce un número entero positivo.")
            
            comprobacion =  numero_entero
            if numero_entero != None:
                condicion = False
        except ValueError as mensaje:
            print(mensaje)
        
    return comprobacion  


def main():
    
    altura = comprobar_numero()
    
    if par_o_impar(altura):  
        triangulo = crear_triangulo_impar(altura)
    else:
        triangulo = crear_triangulo_par(altura)

    print(triangulo)
    
if __name__ == "__main__":  
    main()
