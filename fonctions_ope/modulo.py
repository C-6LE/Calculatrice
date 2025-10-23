def modulo(number_1: int | float, number_2: int | float) -> int | float:
    """
    Fonction modulo qui permet d'obtenir le reste de la division entre deux nombres.

    [Arguments]
    - number_1: int|float = premier nombre choisi par l'utilisateur
    - number_2: int|float = deuxième nombre choisi par l'utilisateur

    [Return]
    - return: le reste de la division de number_1 par number_2
    """
    return number_1 - number_2 * (number_1 // number_2)