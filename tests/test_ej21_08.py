from src.ej21_08 import determinar_tipo

def test_determinar_tipo(tipo):
    assert determinar_tipo(0.0) == "Inaceptable"
    assert determinar_tipo(0.25) == "Aceptable"
    assert determinar_tipo(0.75) == "Meritorio"
    
    