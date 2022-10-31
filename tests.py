import unittest
from ahorcado import Ahorcado
global JUEGO
JUEGO = Ahorcado('hola')

class TestArriesgarPalabra(unittest.TestCase): 
    def test_palabra_correcta(self):
        """ 
        Test Palabra correcta
        """
        resultado = JUEGO.arriesgar_palabra('hola')
        self.assertTrue(resultado)

    def test_palabra_equivocada(self):
        """ 
        Test palabra equivocada
        """
        resultado = JUEGO.arriesgar_palabra('chau')
        self.assertFalse(resultado)    
class TestArriesgarLetra(unittest.TestCase):    
    def test_letra_correcta(self):
        """ 
        Test letra correcta
        """
        resultado = JUEGO.arriesga_letra("h")
        self.assertTrue(resultado)

    def test_letra_incorrecta(self):
        """ 
        Test letra incorrecta
        """
        resultado = JUEGO.arriesga_letra("x")
        self.assertFalse(resultado)

    def test_vida_perdida(self):
        """ 
        Test letra correcta
        """
        JUEGO.arriesga_letra("x")
        self.assertLess(JUEGO.get_vidas(), 5)



if __name__ == '__main__':
    unittest.main()
