def leer_monto():
    return float(input("Introduce un monto (0 para terminar): "))


def procesar_montos():
    total = 0
    bandera = True

    while bandera:
        try:
            monto = leer_monto()  
            
            if monto == 0:  
                bandera =  False
            
            if monto < 0:  
                print("Por favor introduce un monto positivo.")
                
            total += monto 

        except ValueError:
            print("**ERROR**\nIntroduce un número válido.")
    
    return total  


def aplicar_descuento(total):

    if total > 1000:
        descuento = total * 0.10  
        total -= descuento 

    return total  


def mostrar_total(total):
    print(f"El total a pagar es: {total:.2f}")


def main():
    total = procesar_montos()  
    total_con_descuento = aplicar_descuento(total) 
    mostrar_total(total_con_descuento)  

if __name__ == "__main__":
    main()
