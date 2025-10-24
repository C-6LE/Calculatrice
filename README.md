# 🧮 Calculatrice Python

Projet d'initiation à la collaboration sur GitHub - Une calculatrice en ligne de commande simple et modulaire.

## 📋 Description

Ce projet est une calculatrice en Python développée dans le cadre d'un apprentissage de la collaboration sur GitHub. Elle permet d'effectuer des opérations mathématiques de base via une interface en ligne de commande.

## ✨ Fonctionnalités

La calculatrice propose 8 opérations mathématiques :

- ➕ **Addition** : Additionner deux nombres
- ➖ **Soustraction** : Soustraire deux nombres
- ✖️ **Multiplication** : Multiplier deux nombres
- ➗ **Division** : Diviser deux nombres
- 🔢 **Puissance** : Élever un nombre à une puissance
- 📐 **Modulo** : Obtenir le reste d'une division
- 📈 **Exponentielle** : Calculer l'exponentielle d'un nombre
- √ **Racine carrée** : Calculer la racine carrée d'un nombre

## 🚀 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/C-6LE/Calculatrice.git
cd Calculatrice
```

2. Assurez-vous d'avoir Python 3.10+ installé :
```bash
python --version
```

## 💻 Utilisation

Lancez le programme avec :
```bash
python main.py
```

Suivez les instructions à l'écran :
1. Choisissez l'opération souhaitée (1-6)
2. Entrez le premier nombre
3. Entrez le deuxième nombre
4. Le résultat s'affiche automatiquement

### Exemple d'utilisation

```
=== Calculatrice ===
1 - Addition
2 - Soustraction
3 - Multiplication
4 - Division
5 - Puissance
6 - Modulo
7 - Racine carrée
8 - Exponentielle
9 - Quitter


Veuillez choisir votre opération.
> 1
Veuillez entrer votre premier nombre.
> 10
Veuillez entrer votre deuxième nombre.
> 5
10 + 5 = 15
```

## 📁 Structure du projet

```
.
├── fonctions_ope/
│   ├── addition.py
│   ├── soustraction.py
│   ├── multiplication.py
│   ├── division.py
│   ├── puissance.py
│   └── modulo.py
│   └── exponentielle.py
│   └── racine_carre.py
├── main.py
└── README.md
```

Chaque fonction mathématique est isolée dans son propre module pour faciliter la maintenance et la collaboration.

## 👥 Contributeurs

- **Dylan Duchemin** - [HardstyIe](https://github.com/HardstyIe)
- **Cécile Guislain** - [C-6LE](https://github.com/C-6LE)
- **Brian Grumermer** - [briangrumermer](https://github.com/briangrumermer)

## 🎯 Objectifs pédagogiques

Ce projet a été créé pour apprendre :
- La collaboration via Git et GitHub
- La gestion des branches
- Les pull requests et code reviews
- La résolution de conflits
- L'organisation modulaire du code Python

## 📝 Licence

Ce projet est libre de droits et destiné à un usage éducatif.

## 🔮 Améliorations futures

- [ ] Ajout d'un historique des calculs
- [ ] Support des opérations en chaîne
- [ ] Interface graphique (GUI)
- [ ] Gestion des erreurs de saisie
- [ ] Support des nombres complexes
- [ ] Tests unitaires

---

*Projet réalisé dans le cadre d'un apprentissage de GitHub*