#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list# Affecte une valeur à 'replace_in_list'

my_list = [1, 2, 3, 4, 5]# Affecte une valeur à 'my_list'
idx = 3# Affecte une valeur à 'idx'
new_element = 9# Affecte une valeur à 'new_element'
new_list = replace_in_list(my_list, idx, new_element)# Affecte une valeur à 'new_list'

print(new_list)# Affiche à l'écran
print(my_list)# Affiche à l'écran
