from behave import *
from ahorcado import Ahorcado

@given('Una partida con una palabra a adivinar')
def step_partida(self):
    global juego
    juego = Ahorcado('hola')

@when('Ingreso una letra que forma parte de la palabra')
def step_letra_correcta(context):
    global resultado
    resultado = juego.arriesga_letra('h')

@when('Ingreso una letra que no pertenece a la palabra')
def step_letra_correcta(context):
    global resultado
    resultado = juego.arriesga_letra('x')

@when('Ingreso la palabra en cuestion')
def step_palabra_correcta(context):
    global resultado
    resultado = juego.arriesgar_palabra('hola')

@when('Ingreso una palabra incorrecta')
def step_palabra_correcta(context):
    global resultado
    resultado = juego.arriesgar_palabra('chau')

@then('Se muestra mensaje de felicitacion porque adivine la letra')
def step_resultado(context):
    if resultado:
        return 'Bien! Letra correcta'

@then('Se muestra mensaje de error porque la letra es equivocada')
def step_resultado(context):
    if not resultado:
        return 'Error! Letra equivocada'
        
@then('Se muestra un mensaje diciendo que gane el juego')
def step_victoria(context):
    if resultado:
        return 'Respuesta correcta! Felicitaciones!'

@then('Se muestra mensaje diciendo que perdi el juego')
def step_game_over(context):
    if not resultado:
        return 'Palabra incorrecta. Fin del juego!'