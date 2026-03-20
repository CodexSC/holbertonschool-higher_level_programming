#!/usr/bin/python3
Square = __import__('2-square').Square# Affecte une valeur à 'Square'

my_square_1 = Square(3)# Affecte une valeur à 'my_square_1'
print(type(my_square_1))# Affiche à l'écran
print(my_square_1.__dict__)# Affiche à l'écran

my_square_2 = Square()# Affecte une valeur à 'my_square_2'
print(type(my_square_2))# Affiche à l'écran
print(my_square_2.__dict__)# Affiche à l'écran

try:# Bloc try
    print(my_square_1.size)    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)    # Affiche à l'écran

try:# Bloc try
    print(my_square_1.__size)    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)    # Affiche à l'écran

try:# Bloc try
    my_square_3 = Square("3")    # Affecte une valeur à 'my_square_3'
    print(type(my_square_3))    # Affiche à l'écran
    print(my_square_3.__dict__)    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)    # Affiche à l'écran

try:# Bloc try
    my_square_4 = Square(-89)    # Affecte une valeur à 'my_square_4'
    print(type(my_square_4))    # Affiche à l'écran
    print(my_square_4.__dict__)    # Affiche à l'écran
except Exception as e:# Capture l'exception
    print(e)    # Affiche à l'écran
