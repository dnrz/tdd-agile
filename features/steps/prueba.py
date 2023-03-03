import random
from behave import given, when, then
from ahorcado import Ahorcado

PALABRAS = ['hola']
JUEGO = Ahorcado(random.choice(PALABRAS))
RESULTADO = True

@given('Una partida con una palabra a adivinar')
def step_partida():
    global JUEGO
    JUEGO = Ahorcado(random.choice(PALABRAS))
@when('Ingreso una letra que forma parte de la palabra')
def step_letra_correcta():
    global RESULTADO
    RESULTADO = JUEGO.arriesga_letra('h')
@when('Ingreso una letra que no pertenece a la palabra')
def step_letra_incorrecta():
    global RESULTADO
    RESULTADO = JUEGO.arriesga_letra('x')
@when('Ingreso la palabra en cuestion')
def step_palabra_correcta():
    global RESULTADO
    RESULTADO = JUEGO.arriesgar_palabra('hola')
@when('Ingreso una palabra incorrecta')
def step_palabra_incorrecta():
    global RESULTADO
    RESULTADO = JUEGO.arriesgar_palabra('chau')
@then('Se muestra mensaje de felicitacion porque adivine la letra')
def step_resultado_correcto():
    if RESULTADO:
        return 'Bien! Letra correcta'
    return None
@then('Se muestra mensaje de error porque la letra es equivocada')
def step_resultado_incorrecto():
    if not RESULTADO:
        return 'Error! Letra equivocada'
    return None
@then('Se muestra un mensaje diciendo que gane el juego')
def step_victoria():
    if RESULTADO:
        return 'Respuesta correcta! Felicitaciones!'
    return None
@then('Se muestra mensaje diciendo que perdi el juego')
def step_game_over():
    if not RESULTADO:
        return 'Palabra incorrecta. Fin del juego!'
    return None