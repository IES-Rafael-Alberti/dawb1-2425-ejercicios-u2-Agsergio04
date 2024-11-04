from src.ej21_05 import comprobar_edad,comprobar_tributacion

def test_comprobar_edad(edad):
    assert comprobar_edad(18) == True
    assert comprobar_edad(135) == False
    assert comprobar_edad(13) == False

def test_comprobar_tributacion(dinero):
    assert comprobar_tributacion(12000) == True
    assert comprobar_tributacion(500) == False