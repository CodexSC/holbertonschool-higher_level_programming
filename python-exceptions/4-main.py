#!/usr/bin/python3
list_division = __import__('4-list_division').list_division# Affecte une valeur à 'list_division'

my_l_1 = [10, 8, 4]# Affecte une valeur à 'my_l_1'
my_l_2 = [2, 4, 4]# Affecte une valeur à 'my_l_2'
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))# Affecte une valeur à 'result'
print(result)# Affiche à l'écran

print("--")# Affiche à l'écran

my_l_1 = [10, 8, 4, 4]# Affecte une valeur à 'my_l_1'
my_l_2 = [2, 0, "H", 2, 7]# Affecte une valeur à 'my_l_2'
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))# Affecte une valeur à 'result'
print(result)# Affiche à l'écran
