#!/usr/bin/python3

# Retourne une copie de la liste avec l'élément remplacé à l'index `idx`
def new_in_list(my_list, idx, element):  # Définit la fonction 'new_in_list'
    """Crée une nouvelle liste avec l'élément remplacé à l'index spécifié.

    :param my_list: La liste d'éléments.
    :type my_list: list

    :param idx: L'index de l'élément à remplacer.
    :type idx: int

    :param element: Le nouvel élément à insérer.
    :type element: Any

    :return: Une nouvelle liste avec l'élément remplacé ou la liste originale si l'index est invalide.
    :rtype: list
    """
    # Si l'index est négatif, retourne une copie inaltérée
    if idx < 0:  # Condition si
        return my_list[:]  # Retourne le résultat

    # Si l'index est hors limites, retourne une copie inaltérée
    if idx >= len(my_list):  # Condition si
        return my_list[:]  # Retourne le résultat

    # Crée une copie de la liste et remplace l'élément à l'index demandé
    new_list = my_list[:]  # Affecte une valeur à 'new_list'
    new_list[idx] = element  # Affecte une valeur à 'new_list[idx]'
    return new_list  # Retourne le résultat
