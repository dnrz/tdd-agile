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
        resultado = juego.arriesgaLetra("h")
        vidas1 = juego.getVidas()
        resultado = juego.arriesgaLetra("x")
        vidas2 = juego.getVidas()
        self.assertNotEqual(vidas1, vidas2)



if __name__ == '__main__':
    unittest.main()