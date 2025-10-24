def division(number_1: int|float, number_2: int|float) -> int|float :
    """
    Fonction division qui permet de diviser 2 chiffre et obtenir le resultat

    [Arguments]
    - number_1: int|float = nombre 1 choisit par l'utilisateur
    - number_2: int|float = nombre 2 choisit par l'utilisateur

    [Return]
    - return number_1 diviser par number_2
    """
    if number_2 == 0 :
        print("Division par 0 impossible")
        return None
    return number_1/number_2
