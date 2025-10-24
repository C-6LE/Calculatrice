# fonctions_ope/exponentielle.py
import math

def exponentielle(nombre: float) -> float:
    """
    Calcule l'exponentielle e^x d'un nombre donné.
    
    [Arguments]
    - nombre : float -> valeur dont on veut calculer e^x

    [Return]
    - float : e^x
    """
    return math.exp(nombre)