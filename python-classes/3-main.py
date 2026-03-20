#!/usr/bin/python3
# Importe la classe `Square` depuis '3-square'
Square = __import__('3-square').Square  # Affecte une valeur à 'Square'

# Crée un carré de taille 3 et affiche son aire
my_square_1 = Square(3)  # Affecte une valeur à 'my_square_1'
print("Area: {}".format(my_square_1.area()))  # Affiche à l'écran

try:  # Teste l'accès à la propriété `size`
    print(my_square_1.size)  # Affiche à l'écran
except Exception as e:  # Capture l'exception si elle survient
    print(e)  # Affiche à l'écran

try:  # Teste l'accès direct à l'attribut privé (devrait échouer)
    print(my_square_1.__size)  # Affiche à l'écran
except Exception as e:  # Capture l'exception
    print(e)  # Affiche à l'écran

# Crée un second carré et affiche son aire
my_square_2 = Square(5)  # Affecte une valeur à 'my_square_2'
print("Area: {}".format(my_square_2.area()))  # Affiche à l'écran
