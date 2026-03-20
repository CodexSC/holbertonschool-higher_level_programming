#!/usr/bin/python3

# Retourne une liste de booléens indiquant si chaque élément est divisible par 2
def divisible_by_2(my_list=[]):  # Définit la fonction 'divisible_by_2'
    """Retourne une liste de booléens indiquant si chaque élément de la liste `my_list` est divisible par 2.

    :param my_list: La liste d'éléments à analyser.
    :type my_list: list

    :return: Une liste de booléens où chaque élément correspond à la divisibilité par 2 de l'élément à même index dans `my_list`.
    :rtype: list of bool
    """
    # Utilise une compréhension de liste pour tester la divisibilité par 2
    return [num % 2 == 0 for num in my_list]  # Retourne le résultat
