from src.ej21_06 import definir_genero,elegir_aula

def test_elegir_aula(entrada,genero):
    assert elegir_aula("hombre","M") == "A"
    assert elegir_aula("hombre","A") == "B"
    assert elegir_aula("mujer","X") == "A"
    assert elegir_aula("mujer","A") == "B"

def test_definir_genero(entrada):
    assert definir_genero("mujer") == "mujer"
    assert definir_genero("hombre") == "hombre"
    assert definir_genero("hola") == None