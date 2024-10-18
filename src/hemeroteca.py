""" 
Funcion para comprobar un numereo introducido
"""
def comprobar_numero(numero: str) -> bool:
    if numero.startswith("-"):
        numero = numero[1:]
    
        
    return  numero.isdigit()

        