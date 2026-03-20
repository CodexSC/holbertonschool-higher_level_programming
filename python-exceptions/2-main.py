#!/usr/bin/python3
safe_print_list_integers = \# Affecte une valeur à 'safe_print_list_integers'
    __import__('2-safe_print_list_integers').safe_print_list_integers    # Code

my_list = [1, 2, 3, 4, 5]# Affecte une valeur à 'my_list'

nb_print = safe_print_list_integers(my_list, 2)# Affecte une valeur à 'nb_print'
print("nb_print: {:d}".format(nb_print))# Affiche à l'écran

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]# Affecte une valeur à 'my_list'
nb_print = safe_print_list_integers(my_list, len(my_list))# Affecte une valeur à 'nb_print'
print("nb_print: {:d}".format(nb_print))# Affiche à l'écran

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)# Affecte une valeur à 'nb_print'
print("nb_print: {:d}".format(nb_print))# Affiche à l'écran
