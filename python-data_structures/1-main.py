#!/usr/bin/python3
element_at = __import__('1-element_at').element_at# Affecte une valeur à 'element_at'
my_list = [1, 2, 3, 4, 5]# Affecte une valeur à 'my_list'
idx = 3# Affecte une valeur à 'idx'
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))# Affiche à l'écran
