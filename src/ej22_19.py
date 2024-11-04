def mostrar_menu():
    print("Menú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")


def comenzar_programa():
    print("Programa comenzado.")


def imprimir_listado():
    print("Imprimiendo listado...")


def main():
    bandera = True

    mostrar_menu()
    print("Selecciona una opción (1, 2 o 3):\n")
    
    while bandera:
          
        opcion = input()  

        try:
            if opcion == '1':
                comenzar_programa()  
            elif opcion == '2':
                imprimir_listado()  
            elif opcion == '3':
                print("Finalizando el programa.")
                bandera = False  
            else:
                raise ValueError("Opcion incorrecta,selecciona 1, 2 o 3.")
        
        except ValueError as e:
            print(f"**ERROR**\n{e}")

if __name__ == "__main__":
    main()
