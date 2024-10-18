def division_numero(numerador : str,denominador : str) -> float:
    div_resultado = 0
    try:
        div_resultado = float(numerador) / float(denominador)
    except ZeroDivisionError:
        print("**ERROR**\nNo se puede dividir por 0.")
    
    return div_resultado
def main():
    numerador = input("Introduce")
if __name__ == "__main__":
    main()