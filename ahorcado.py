class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 5
    def get_vidas(self):
        """ 
        Get vidas 
        """
        return self.vidas

    def arriesgar_palabra(self, palabra_sugerida):
        """ 
        Arriesgar Palabras 
        """
        if self.palabra == palabra_sugerida:
            return True
        return False

    def arriesga_letra(self, letra_sugerida):
        """ 
        Arriesgar Letra 
        """
        palabra_jugador = []
        respuesta = False
        for i in range(len(self.palabra)-1):
            palabra_jugador.append(0)

        for i in range(len(self.palabra)-1):
            if self.palabra[i] == letra_sugerida:
                palabra_jugador[i] = letra_sugerida
                respuesta = True
        if not respuesta:
            self.vidas -= 1

        return respuesta

