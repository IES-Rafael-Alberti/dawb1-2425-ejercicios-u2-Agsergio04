def es_primo(numero):
    condicion = True
    if numero <= 1:
        condicion = False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            condicion = False

    return condicion 

def main():
    cantidad_primos = 0  
    bandera = True
    
    while bandera:
        try:
            numero = int(input("Ingrese un número mayor que 1 (0 para terminar): "))

            if numero == 0:
                bandera = False  

            if numero > 1 and es_primo(numero):
                cantidad_primos += 1  
                
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print(f"Se ingresaron {cantidad_primos} números primos.")

if __name__ == "__main__":
    main()
