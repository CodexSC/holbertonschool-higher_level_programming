#!/usr/bin/python3
# Importe la classe Square depuis '6-square'
Square = __import__('6-square').Square  # Affecte une valeur à 'Square'

# Test d'impression sans position (position par défaut)
my_square_1 = Square(3)  # Affecte une valeur à 'my_square_1'
my_square_1.my_print()  # Code

print("--")  # Séparateur visuel

# Test d'impression avec position (offset horizontal=1, vertical=1)
my_square_2 = Square(3, (1, 1))  # Affecte une valeur à 'my_square_2'
my_square_2.my_print()  # Code

print("--")  # Séparateur visuel

# Test d'impression avec position (offset horizontal=3, vertical=0)
my_square_3 = Square(3, (3, 0))  # Affecte une valeur à 'my_square_3'
my_square_3.my_print()  # Code

print("--")  # Séparateur visuel
