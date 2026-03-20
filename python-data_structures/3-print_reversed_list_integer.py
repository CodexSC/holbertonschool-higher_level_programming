#!/usr/bin/python3

# Imprime les éléments d'une liste entière dans l'ordre inversé
def print_reversed_list_integer(my_list=[]):  # Définit la fonction 'print_reversed_list_integer'
    """Imprime les éléments d'une liste entière dans l'ordre inversé.

    :param my_list: La liste d'éléments à imprimer. Par défaut, une liste vide.
    :type my_list: list
    """
    # Parcourt la liste à l'envers (slice [::-1]) et imprime chaque entier
    [print("{:d}".format(item)) for item in my_list[::-1]]  # Code
