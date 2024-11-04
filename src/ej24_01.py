def funcion_burbuja(lista):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja.

    El algoritmo de burbuja compara pares de elementos adyacentes en la lista
    y los intercambia si están en el orden incorrecto. Este proceso se repite
    hasta que la lista queda ordenada.

    Parametros:
    lista (list): Una lista de números que se desea ordenar.

    Retorna:
    list: La lista ordenada de menor a mayor.
    
    Ejemplo:
    >>> funcion_burbuja([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
    """
    tamanio = len(lista)

    for i in range(tamanio):
        for j in range(0, tamanio-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


def main():
    """
    Funcion principal que ejecuta el programa.

    Crea una lista de números, la copia, y luego llama a la funcion
    "funcion_burbuja" para ordenarla. Finalmente, imprime la lista
    ordenada en la consola.
    
    Ejemplo de uso:
    >>> main()
    La lista ordenada es: [1, 3, 8, 14, 19]
    """
    a = [8, 3, 1, 19, 14]
    
    lista = a.copy()  # Copia la lista original
    lista_ordenada = funcion_burbuja(lista)

    print(f"La lista ordenada es: {lista_ordenada}")

if __name__ == "__main__":
    main()
