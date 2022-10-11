import unittest
from ahorcado import Ahorcado
import unittest

class TestArriesgarPalabra(unittest.TestCase):
    
    def test_PalabraCorrecta(self):
        juego = Ahorcado('hola')
        resultado = juego.arriesgarPalabra('hola')
        self.assertTrue(resultado)

    def test_PalabraEquivocada(self):
        juego = Ahorcado('hola')
        resultado = juego.arriesgarPalabra('chau')
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()