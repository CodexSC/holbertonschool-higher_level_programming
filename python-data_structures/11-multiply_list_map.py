#!/usr/bin/python3

# Multiplie chaque élément d'une liste par un nombre et retourne une nouvelle liste
def multiply_list_map(my_list=[], number=0):  # Définit la fonction 'multiply_list_map'
    """Multiplie chaque élément de la liste `my_list` par un nombre donné et retourne une nouvelle liste avec les résultats.

    :param my_list: La liste d'éléments à multiplier.
    :type my_list: list

    :param number: Le nombre par lequel chaque élément de la liste doit être multiplié. Par défaut, 0.
    :type number: int

    :return: Une nouvelle liste contenant les résultats des multiplications.
    :rtype: list
    """
    # Utilise map + lambda pour produire une nouvelle liste multipliée
    return list(map(lambda x: x * number, my_list))  # Retourne le résultat
