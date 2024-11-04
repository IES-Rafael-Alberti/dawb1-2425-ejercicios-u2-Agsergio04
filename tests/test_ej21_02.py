from src.ej21_02 import comprobar_contrasenia

def test_comprobar_contrasenia(entrada,contrase):
    assert comprobar_contrasenia("hola","adios") == False
    assert comprobar_contrasenia("hola","hola") == True