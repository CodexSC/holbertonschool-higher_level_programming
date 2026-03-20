#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at# Affecte une valeur à 'delete_at'

my_list = [1, 2, 3, 4, 5]# Affecte une valeur à 'my_list'
idx = 3# Affecte une valeur à 'idx'
new_list = delete_at(my_list, idx)# Affecte une valeur à 'new_list'
print(new_list)# Affiche à l'écran
print(my_list)# Affiche à l'écran
