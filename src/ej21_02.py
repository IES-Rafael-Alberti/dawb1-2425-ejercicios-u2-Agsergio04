"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
"""
def main():
    bandera = True
    contrasenia = "python"
    
    while bandera:
        pregunta = input("Introduce la contraseña: ").lower()

        if pregunta == contrasenia:
            bandera = False
        else:
            print("Contraseña incorrecta.")
    
    print("Felicidades,has introducido la contraseña.")
    
if __name__ == "__main__":
    main()