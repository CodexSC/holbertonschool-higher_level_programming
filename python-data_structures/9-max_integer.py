#!/usr/bin/python3

# Retourne la valeur maximale d'une liste, ou None si la liste est vide
def max_integer(my_list=[]):  # Définit la fonction 'max_integer'
    """Retourne l'élément maximum d'une liste. Si la liste est vide, retourne None.

    :param my_list: La liste d'éléments à analyser.
    :type my_list: list

    :return: L'élément maximum de la liste ou `None` si la liste est vide.
    :rtype: Any
    """
    # Si la liste est vide, retourne None
    if len(my_list) == 0:  # Condition si
        return None  # Retourne le résultat

    # Initialise le maximum avec le premier élément
    max_value = my_list[0]  # Affecte une valeur à 'max_value'

    # Parcourt les éléments restants pour trouver le plus grand
    for i in range(1, len(my_list)):  # Boucle pour
        if my_list[i] > max_value:  # Condition si
            max_value = my_list[i]  # Affecte une valeur à 'max_value'

    # Retourne le maximum trouvé
    return max_value  # Retourne le résultat
