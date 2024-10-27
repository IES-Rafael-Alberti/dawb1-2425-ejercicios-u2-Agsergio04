def leer_numero():
    return int(input("Introduce un número entero positivo (0 para terminar): "))


def contar_digitos(numero):
    pares = 0
    impares = 0

    for digito in str(numero):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

def main():
    total_pares = 0
    total_impares = 0
    bandera = True

    while bandera:
        try:
            numero = leer_numero() 
            
            if numero == 0: 
                bandera = False
            
            if numero < 0:
                print("Por favor, introduce un numero entero positivo.")
                
            
            pares, impares = contar_digitos(numero)  
            print(f"El número {numero} tiene {pares} dígitos pares y {impares} dígitos impares.")
            
            total_pares += pares
            total_impares += impares

        except ValueError:
            print("**ERROR**\nIntroduce solo numeros enteros.")

   
    print(f"Total de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")

if __name__ == "__main__":
    main()
