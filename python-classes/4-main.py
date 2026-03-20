#!/usr/bin/python3
# Importe la classe `Square` depuis '4-square'
Square = __import__('4-square').Square  # Affecte une valeur à 'Square'

# Crée un carré de taille 89 et affiche son aire et sa taille
my_square = Square(89)  # Affecte une valeur à 'my_square'
print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Affiche à l'écran

# Modifie la taille via la propriété et affiche à nouveau l'aire
my_square.size = 3  # Affecte une valeur à 'my_square.size'
print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Affiche à l'écran

try:  # Tente d'assigner une valeur invalide (chaîne) à la propriété size
    my_square.size = "5 feet"  # Affecte une valeur à 'my_square.size'
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Affiche à l'écran
except Exception as e:  # Capture l'exception (TypeError attendu)
    print(e)  # Affiche à l'écran
