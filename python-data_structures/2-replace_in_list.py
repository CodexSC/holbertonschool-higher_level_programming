#!/usr/bin/python3

# Remplace l'élément à l'index `idx` dans `my_list` si l'index est valide
def replace_in_list(my_list, idx, element):  # Définit la fonction 'replace_in_list'
    """Remplace l'élément à l'index spécifié dans la liste `my_list`.

    :param my_list: La liste d'éléments.
    :type my_list: list

    :param idx: L'index de l'élément à remplacer.
    :type idx: int

    :param element: Le nouvel élément à insérer.
    :type element: Any

    :return: La liste modifiée ou la liste originale si l'index est invalide.
    :rtype: list
    """
    # Si l'index est négatif, ne rien faire
    if idx < 0:  # Condition si
        return my_list  # Retourne le résultat

    # Si l'index est hors limites, ne rien faire
    if idx >= len(my_list):  # Condition si
        return my_list  # Retourne le résultat

    # Remplace l'élément à l'index donné
    my_list[idx] = element  # Affecte une valeur à 'my_list[idx]'
    return my_list  # Retourne le résultat
