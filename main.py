from fonctions_ope.addition import addition
from fonctions_ope.soustraction import soustraction
from fonctions_ope.multiplication import multiplication
from fonctions_ope.division import division
from fonctions_ope.puissance import puissance
from fonctions_ope.modulo import modulo

print("=== Calculatrice ===")
print("1 - Addition")
print("2 - Soustraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Puissance")
print("6 - Modulo")

choice = int(input("Veuillez choisir votre opération.\n"))

match choice: 
    case 1:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} + {number_2} = {addition(number_1 , number_2)}")
    case 2:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} - {number_2} = {soustraction(number_1 , number_2)}")
    case 3:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} x {number_2} = {multiplication(number_1 , number_2)}")
    case 4:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} / {number_2} = {division(number_1 , number_2)}")
    case 5:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} ^ {number_2} = {puissance(number_1 , number_2)}")
    case 6:
        number_1 = int(input("Veuillez entrer votre premier nombre. \n"))
        number_2 = int(input("Veuillez entrer votre deuxième nombre. \n"))
        print(f"{number_1} % {number_2} = {modulo(number_1 , number_2)}")

