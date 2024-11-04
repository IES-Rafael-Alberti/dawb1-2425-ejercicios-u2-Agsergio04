def numero_primo(numero):
    comprobacion = True

    if numero > 2:
        for valor in range(2,int(numero**0.5) + 1):
            if (numero % valor == 0):
                comprobacion = False

    
    return comprobacion


def pedir_usuario():
     return int(input("Introduce un numero entero: "))


def main():
    bandera = True

    while bandera:
            try:
                numero = pedir_usuario() 

            except ValueError:
                print("**ERROR**\nIntroduce un parametro valido.")
            else:
                if numero_primo(numero):
                     print(f"{numero} es un numero primo")
                else:
                     print(f"{numero} no es un numero primo")
                
if __name__ == "__main__":
     main()