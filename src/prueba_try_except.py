def introducir_numero(cadena: str) -> bool:
    
    num = float(input(cadena))
    return num        
            


def main():
    try:
        num = introducir_numero("Itroduzca un numero: ")
        divisor = introducir_numero("Itroduzca otro numero: ")
        
        resultado = num / divisor
        
    except ValueError:
        print("*ERROR* el numero no es valido.")
    except ZeroDivisionError:
        print("*ERROR* no se puede dividir entre 0.")
    
    if num is not None:
        print(f"El numero que has escrito es {resultado:.2f}")
if __name__ == "__main__":
    main()