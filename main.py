from fonctions_ope.addition import addition
from fonctions_ope.soustraction import soustraction
from fonctions_ope.multiplication import multiplication
from fonctions_ope.division import division
from fonctions_ope.puissance import puissance
from fonctions_ope.modulo import modulo
from fonctions_ope.racine_carree import racine_carree
from fonctions_ope.exponentielle import exponentielle

def demander_nombres(text: str) -> float:

    """
    Fonction qui demande a l'utilisateur un nombre.

    [Arguments]
    - text: str = texte qui demande a l'utilisateur de rentrer un nombre

    [Return]
    - un float qui correspond a l'entrée de l'utilisateur
    """

    while True:
        try:
            return float(input(text))
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
    print("7 - Racine carrée")
    print("8 - Exponentielle (e^x)")  
    print("9 - Quitter")

resultat_precedent = None

#Boucle qui permet de rejouer en boucle le calcul d'un type d'opération
while True:

    afficher_menu()

    try:
        choice = int(input("Veuillez choisir votre opération.\n"))
    except ValueError:
            print("Entrée invalide")

    if choice == 7:
            number_1 = demander_nombres("Veuillez entrer votre nombre \n")
           

    elif resultat_precedent is not None:
        print(f"\n resultat actuel : {resultat_precedent}")
        utiliser = input(f"Souhaitez-vous utilisez {resultat_precedent} comme premier nombre ? (o / n)\n").lower()
        if utiliser == "o":
            number_1 = resultat_precedent
        else:
            number_1 = demander_nombres("Veuillez entrer votre premier nombre \n")
       
    else:
        number_1 = demander_nombres("Veuillez entrer votre premier nombre \n")
    if choice != (7, 8):
        number_2 = demander_nombres("Veuillez entrer votre deuxieme nombre \n")


    match choice: 
        case 1:
            resultat_precedent = addition(number_1, number_2)
            print(f"{number_1} + {number_2} = {resultat_precedent}")
        case 2:
            resultat_precedent = soustraction(number_1, number_2)
            print(f"{number_1} - {number_2} = {resultat_precedent}")
        case 3:
            resultat_precedent = multiplication(number_1, number_2)
            print(f"{number_1} x {number_2} = {resultat_precedent}")
        case 4:
            resultat_precedent = division(number_1, number_2)
            print(f"{number_1} / {number_2} = {resultat_precedent}")
        case 5:
            resultat_precedent = puissance(number_1, number_2)
            print(f"{number_1} ^ {number_2} = {resultat_precedent}")
        case 6:
            resultat_precedent = modulo(number_1, number_2)
            print(f"{number_1} % {number_2} = {resultat_precedent}")
        case 7:
            resultat_precedent = racine_carree(number_1)
            print (f" √{number_1} = {resultat_precedent}")
        case 8:
            resultat_precedent = exponentielle(number_1)
            print(f"e^{number_1} = {resultat_precedent}")
        case 9:
            print("Fin de programme")
            break