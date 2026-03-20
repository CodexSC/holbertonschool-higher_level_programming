#!/usr/bin/python3
# Imprime chaque entier d'une liste, un par ligne
def print_list_integer(my_list=[]):  # Définit la fonction 'print_list_integer'
    """Imprime chaque entier de `my_list` suivi d'un saut de ligne."""  # Docstring courte
    # Parcourt chaque entier de la liste fournie
    for integer in my_list:  # Boucle pour
        # Formate et affiche l'entier (format décimal sans autres caractères)
        print("{:d}".format(integer))  # Affiche à l'écran
