#!/usr/bin/python3

# Supprime l'élément situé à l'index `idx` dans `my_list` si l'index est valide
def delete_at(my_list=[], idx=0):  # Définit la fonction 'delete_at'
    """Supprime l'élément à l'index spécifié dans la liste `my_list`.

    Si l'index est invalide, la fonction retourne la liste sans modification.

    :param my_list: La liste d'éléments.
    :type my_list: list

    :param idx: L'index de l'élément à supprimer. Par défaut, 0.
    :type idx: int

    :return: La liste modifiée ou la liste originale si l'index est invalide.
    :rtype: list
    """

    # Si l'index est négatif ou hors limites, ne rien faire
    if idx < 0 or idx >= len(my_list):  # Condition si
        return my_list  # Retourne le résultat

    # Supprime l'élément à l'index spécifié
    del my_list[idx]  # Code

    # Retourne la liste (modifiée)
    return my_list  # Retourne le résultat
