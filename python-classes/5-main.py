#!/usr/bin/python3

# Importe la classe Square depuis '5-square'
Square = __import__('5-square').Square  # Affecte une valeur à 'Square'

# Crée un carré de taille 3 et l'affiche via my_print()
my_square = Square(3)  # Affecte une valeur à 'my_square'
my_square.my_print()  # Code

print("--")  # Séparateur visuel

# Modifie la taille à 10 et imprime
my_square.size = 10  # Affecte une valeur à 'my_square.size'
my_square.my_print()  # Code

print("--")  # Séparateur visuel

# Régle la taille à 0 et imprime (doit afficher une ligne vide)
my_square.size = 0  # Affecte une valeur à 'my_square.size'
my_square.my_print()  # Code
