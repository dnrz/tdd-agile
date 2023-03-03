Feature: corriendo tests de aceptacion

  Scenario: Adivino una letra
     Given Una partida con una palabra a adivinar
     When Ingreso una letra que forma parte de la palabra
     Then Se muestra mensaje de felicitacion porque adivine la letra

  Scenario: Me equivoco de letra
    Given Una partida con una palabra a adivinar
    When Ingreso una letra que no pertenece a la palabra
    Then Se muestra mensaje de error porque la letra es equivocada

  Scenario: Arriesgo con la palabra correcta
    Given Una partida con una palabra a adivinar
    When Ingreso la palabra en cuestion
    Then Se muestra un mensaje diciendo que gane el juego

  Scenario: Arriesgo con una palabra equivocada
    Given Una partida con una palabra a adivinar
    When Ingreso una palabra incorrecta
    Then Se muestra mensaje diciendo que perdi el juego