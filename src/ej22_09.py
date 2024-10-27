def pedir_contraseña():
    parametro = input("Introduce la contraseña: ")
    return parametro

def comprobar_contrasenia(contrasenia,pregunta):
    comprobacion = True
    
    if contrasenia == pregunta:
        comprobacion = False
        
    return comprobacion
def main():
    contrasenia = "python"
    
    pregunta = pedir_contraseña().lower()
    
    while comprobar_contrasenia(contrasenia,pregunta):
        print("Contraseña incorecta,vuelva a introducirla de nuevo")
        pregunta = pedir_contraseña().lower()
        
    print("\nHas iniciado sesion correctamente")
    
    
if __name__ == "__main__":
    main()