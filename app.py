from flask import Flask, render_template
from ahorcado import Ahorcado

app = Flask(__name__)

@app.route("/")
def index():
    JUEGO = Ahorcado('palabra')
    #for _ in range(len(JUEGO.palabra)):
    #    if JUEGO.vidas > 0:
    #        JUEGO.arriesga_letra('x')
    #        if JUEGO.vidas == 0:
    #            return 'PERDISTE'
	#        blanks = 0
	#        to_display = []
	#	    if char==" ":
	#		    to_display.append(" ")
	#	     else:
	#		    to_display.append("_")
	#		    blanks+=1
    return render_template('game.html',to_display=JUEGO.palabra,tries=JUEGO.vidas)

if __name__ == "__main__":
    app.run()
