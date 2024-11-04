from src.ej21_10 import comprobar_ingrediente

def test_comprobar_ingrediente(numero):
    assert comprobar_ingrediente("pimiento") == True
    assert comprobar_ingrediente("tofu") == True
    assert comprobar_ingrediente("jamon") == True
    assert comprobar_ingrediente("casa") == False