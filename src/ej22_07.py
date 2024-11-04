def tabla_multiplicar(numero):
    for i in range(11):
        print(f"{i} x {numero} = {i * numero}")


def main():
    numero = 10
    print(f"\tEsta es la tabla de multiplicar del {numero}")
    tabla_multiplicar(numero)

if __name__ == "__main__":
    main()