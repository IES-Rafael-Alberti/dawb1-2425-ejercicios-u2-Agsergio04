def pedir_usuario():
    pregunta_1 = float(input("Cuanto desea invertir: "))
    pregunta_2  =float(input("De cuanto es el interes anual: "))
    pregunta_3 =int(input("Cuanto tiempo desea que dure la inversion: "))

    return pregunta_1,pregunta_2,pregunta_3


def calculo_interes(inverison,interes,tiempo):
    for _ in range(tiempo):
        inverison *= 1 + interes / 100

    return inverison


def main():
    bandera = True

    while bandera:
            try:
                inversion, interes, tiempo = pedir_usuario() 
                total = calculo_interes(inversion, interes, tiempo)

            except ValueError:
                print("**ERROR**\nIntroduce un parametro valido.")
            else:
                print(f"Según los {tiempo} años que se va a invertir, el total obtenido sería de {total:.2f} euros")

                salida = input("¿Desea salir (S/N): ")

                if salida.upper() == 'S':
                    bandera = False

if __name__ == "__main__":
    main()