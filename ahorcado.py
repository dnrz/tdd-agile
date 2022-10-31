class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 5
    def get_vidas(self):
        """ 
        Get vidas 
        """
        return self.vidas

    def arriesgar_palabra(self, palabraSugerida):
        """ 
        Arriesgar Palabras 
        """
        if self.palabra == palabraSugerida:
            return True
        return False

    def arriesga_letra(self, letraSugerida):
        """ 
        Arriesgar Letra 
        """
        palabraJugador = []
        respuesta = False
        for i in range(len(self.palabra)-1):
            palabraJugador.append(0)

        for i in range(len(self.palabra)-1):
            if self.palabra[i] == letraSugerida:
                palabraJugador[i] = letraSugerida
                respuesta = True
        if not respuesta:
            self.vidas -= 1

        return respuesta

