#!/usr/bin/python3

# Imprime jusqu'à `x` entiers de `my_list` en ignorant les éléments non entiers
def safe_print_list_integers(my_list=[], x=0):  # Définit la fonction 'safe_print_list_integers'
    """Imprime jusqu'à `x` éléments de `my_list` qui sont des entiers (exclut bool).

    Retourne le nombre d'entiers imprimés.
    """
    count = 0  # Compteur d'entiers imprimés
    for i in range(x):  # Parcourt les indices demandés
        try:  # Tente de récupérer l'élément
            element = my_list[i]  # Affecte une valeur à 'element'
            # Vérifie que l'élément est un entier (exclut bool)
            if isinstance(element, int) and not isinstance(element, bool):  # Condition si
                print("{:d}".format(element), end='')  # Imprime l'entier
                count += 1  # Incrémente le compteur
        except (TypeError, ValueError):  # Ignore les erreurs de format
            pass
    print()  # Fin de ligne
    return count  # Retourne le nombre d'entiers imprimés
