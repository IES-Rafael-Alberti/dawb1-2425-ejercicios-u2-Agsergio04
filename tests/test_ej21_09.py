from src.ej21_09 import calcular_precio

def test_calcular_precio(edad):
    assert calcular_precio(2) == "puedes entrar gratis"
    assert calcular_precio(12) == "para entrar debes pagar 5 euros"
    assert calcular_precio(22) == "para entrar debes pagar 10 euros"