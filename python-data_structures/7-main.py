#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple# Affecte une valeur à 'add_tuple'

tuple_a = (1, 89)# Affecte une valeur à 'tuple_a'
tuple_b = (88, 11)# Affecte une valeur à 'tuple_b'
new_tuple = add_tuple(tuple_a, tuple_b)# Affecte une valeur à 'new_tuple'
print(new_tuple)# Affiche à l'écran

print(add_tuple(tuple_a, (1, )))# Affiche à l'écran
print(add_tuple(tuple_a, ()))# Affiche à l'écran
