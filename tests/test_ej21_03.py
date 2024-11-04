from src.ej21_03 import division_numero

def test_division_numero(num,dem):
    assert division_numero(10,2) == 5
    assert division_numero(20,3) == 6.66666666667