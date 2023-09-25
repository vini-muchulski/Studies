from circle_intervalos import Circulo
import pytest

def test_comprimento_de_arco():
    circulo_test = Circulo(4, 0, 180)
    esperado = 12.566370614359172

    assert circulo_test.comprimento_de_arco() == esperado


def test_get_raio():
    circulo_test = Circulo(4, 0, 180)
    esperado = 4

    assert circulo_test.get_raio() == esperado

def test_area_do_setor_circular():
    circulo_test = Circulo(4, 0, 180)
    esperado = 25.132741228718345

    assert circulo_test.get_setor_area_circle() == esperado