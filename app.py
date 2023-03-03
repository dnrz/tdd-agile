from flask import Flask
from ahorcado import Ahorcado

app = Flask(__name__)

@app.route("/")
def index():
    JUEGO = Ahorcado('palabra')
    for _ in range(len(JUEGO.palabra)):
        if JUEGO.vidas > 0:
            JUEGO.arriesga_letra('x')
            if JUEGO.vidas == 0:
                return 'PERDISTE'



if __name__ == "__main__":
    app.run()
