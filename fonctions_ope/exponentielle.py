# fonctions_ope/exponentielle.py
import math

def exponentielle(number_1: float) -> float:
    """
    Calcule l'exponentielle e^x d'un nombre donné.
    
    [Arguments]
    - nombre : float -> valeur dont on veut calculer e^x

    [Return]
    - float : e^x
    """
    return math.exp(number_1)