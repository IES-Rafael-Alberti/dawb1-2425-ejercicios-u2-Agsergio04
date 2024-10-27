def funcion_burbuja(lista):
    tamanio = len(lista)

    for i in range(tamanio):
        
        for j in range(0, tamanio-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def main():
    a = [8, 3, 1, 19, 14]
    lista = a.copy() # copia la lista
    lista_ordenada = funcion_burbuja(lista)

    print(f"La lista ordenada es: {lista_ordenada}")

if __name__ == "__main__":
    main()
