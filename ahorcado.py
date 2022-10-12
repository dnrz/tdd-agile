class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 5
    
    def getVidas(self):
        return self.vidas

    def arriesgarPalabra(self, palabraSugerida):
        if self.palabra == palabraSugerida:
            return True
        else:
            return False

    def arriesgaLetra(self, letraSugerida):
        palabraJugador = []
        respuesta = False
        for i in range(len(self.palabra)-1):
            palabraJugador.append(0)

        for i in range(len(self.palabra)-1):
            if self.palabra[i] == letraSugerida:
                palabraJugador[i] = letraSugerida
                respuesta = True
        if respuesta == False:
            self.vidas -= 1

        return respuesta

