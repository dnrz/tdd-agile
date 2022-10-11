class Ahorcado:

    vidas = 5

    def __init__(self, palabra):
        self.palabra = palabra

    def arriesgarPalabra(self, palabraSugerida):
        if self.palabra == palabraSugerida:
            return True
        else:
            return False
