#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2# Affecte une valeur à 'divisible_by_2'

my_list = [0, 1, 2, 3, 4, 5, 6]# Affecte une valeur à 'my_list'
list_result = divisible_by_2(my_list)# Affecte une valeur à 'list_result'

i = 0# Affecte une valeur à 'i'
while i < len(list_result):# Boucle tant que
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))    # Affiche à l'écran
    i += 1    # Affecte une valeur à '+'
