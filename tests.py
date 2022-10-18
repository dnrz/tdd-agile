import unittest
from ahorcado import Ahorcado
global juego
juego = Ahorcado('hola')

class TestArriesgarPalabra(unittest.TestCase):
    
    def test_PalabraCorrecta(self):
        resultado = juego.arriesgarPalabra('hola')
        self.assertTrue(resultado)

    def test_PalabraEquivocada(self):
        resultado = juego.arriesgarPalabra('chau')
        self.assertFalse(resultado)
    
class TestArriesgarLetra(unittest.TestCase):
    
    def test_LetraCorrecta(self):
        resultado = juego.arriesgaLetra("h")
        self.assertTrue(resultado)

    def test_LetraIncorrecta(self):
        resultado = juego.arriesgaLetra("x")
        self.assertFalse(resultado)

    def test_VidaPerdida(self):
        juego.arriesgaLetra("x")
        self.assertLess(juego.getVidas(), 5)



if __name__ == '__main__':
    unittest.main()