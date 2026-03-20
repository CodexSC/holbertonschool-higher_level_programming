#!/usr/bin/python3
# Importe la classe `Square` depuis le module '1-square'
Square = __import__('1-square').Square  # Affecte la référence à 'Square' depuis le module

# Instancie un carré avec taille 3
my_square = Square(3)  # Affecte une valeur à 'my_square'
# Affiche le type de l'objet (classe de l'instance)
print(type(my_square))  # Affiche à l'écran
# Affiche le dictionnaire d'attributs de l'objet (état interne)
print(my_square.__dict__)  # Affiche à l'écran

try:  # Tentative d'accès à la propriété `size`
    print(my_square.size)  # Affiche à l'écran
except Exception as e:  # Capture toute exception et affiche le message
    print(e)  # Affiche à l'écran

try:  # Tentative d'accès à l'attribut privé `__size` (devrait échouer)
    print(my_square.__size)  # Affiche à l'écran
except Exception as e:  # Capture l'exception (AttributeError attendu)
    print(e)  # Affiche à l'écran
