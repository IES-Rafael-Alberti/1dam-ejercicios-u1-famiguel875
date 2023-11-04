from prueba1 import obtener_mayor

def test_obtener_mayor():
    assert obtener_mayor(5, 10) == 10
    assert obtener_mayor(20, 5) == 20
    assert obtener_mayor(8, 8) == 0