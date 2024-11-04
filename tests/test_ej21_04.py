from src.ej21_04 import par_o_impar

def test_par_o_impar(numero):
    assert par_o_impar(12) == "par"
    assert par_o_impar(77) == "impar"
