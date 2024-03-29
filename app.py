from flask import Flask, render_template
from ahorcado import Ahorcado

app = Flask(__name__)

@app.route("/")
def index():
    juego = Ahorcado('palabra')
    #for _ in range(len(JUEGO.palabra)):
    #    if JUEGO.vidas > 0:
    #        JUEGO.arriesga_letra('x')
    #        if JUEGO.vidas == 0:
    #            return 'PERDISTE'
    return render_template('game.html',to_display=juego.palabra,tries=juego.vidas)

if __name__ == "__main__":
    app.run()
