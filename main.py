from fonctions_ope.addition import addition
from fonctions_ope.soustraction import soustraction
from fonctions_ope.multiplication import multiplication
from fonctions_ope.division import division
from fonctions_ope.puissance import puissance
from fonctions_ope.modulo import modulo

def demander_nombres() -> tuple[float, float]:

    """
    Fonction qui demande a l'utilisateur de rentrer des nombres.

    [Return]
    - return number_1 et number_2
    """

    while True:

        try: 
            number_1 = float(input("Veuillez entrer votre premier nombre. \n"))
            number_2 = float(input("Veuillez entrer votre deuxieme nombre. \n"))
            return number_1, number_2
        except ValueError:
            print("Entrée invalide")
            continue

def afficher_menu():
    """
    Fonction affichant un menu semblable a une calculatrice
    """
    print("=== Calculatrice ===")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Puissance")
    print("6 - Modulo")
    print("7 - Quitter")

#Boucle qui permet de rejouer en boucle le calcul d'un type d'opération
while True:

    afficher_menu()

    try:
        choice = int(input("Veuillez choisir votre opération.\n"))
    except ValueError:
            print("Entrée invalide")

    match choice: 
        case 1:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} + {number_2} = {addition(number_1 , number_2)}")
        case 2:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} - {number_2} = {soustraction(number_1 , number_2)}")
        case 3:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} x {number_2} = {multiplication(number_1 , number_2)}")
        case 4:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} / {number_2} = {division(number_1 , number_2)}")
        case 5:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} ^ {number_2} = {puissance(number_1 , number_2)}")
        case 6:
            number_1, number_2 = demander_nombres()
            print(f"{number_1} % {number_2} = {modulo(number_1 , number_2)}")
        case 7:
            print("Fin de programme")
            break