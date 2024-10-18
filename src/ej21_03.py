def division_numero(numerador : str,denominador : str) -> float:
    div_resultado = 0
    try:
        div_resultado = float(numerador) / float(denominador)
    except ValueError:
        print("**ERROR**\nO el numerador o el denominador no es valido")
    except ZeroDivisionError:
        print("**ERROR**\nNo se puede dividir por 0.")
        
    return div_resultado

def main():
    #Tengo que crear las variables de la comprobacion del numerador y del denomiador de la hemeroteca
    numerador = input("Introduce el numerador: ")
    denominador = input("Introduce el denominador: ")
    
    resultado = division_numero(numerador,denominador)
    
    print(f"")
if __name__ == "__main__":
    main()