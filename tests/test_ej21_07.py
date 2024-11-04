from src.ej21_07 import calculo_tipo_impositivo

def test_calculo_tipo_impositivo(improvisto):
    assert calculo_tipo_impositivo(-12) == None
    assert calculo_tipo_impositivo(12) == 5
    assert calculo_tipo_impositivo(15000) == 15
    assert calculo_tipo_impositivo(37000) == 35
    assert calculo_tipo_impositivo(120000) == 45