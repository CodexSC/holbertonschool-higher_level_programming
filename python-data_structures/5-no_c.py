#!/usr/bin/python3

# Supprime toutes les occurrences de 'c' et 'C' dans une chaîne
def no_c(my_string):  # Définit la fonction 'no_c'
    """Retire toutes les occurrences des lettres 'c' et 'C' de la chaîne donnée.

    :param my_string: La chaîne de caractères à traiter.
    :type my_string: str

    :return: Une nouvelle chaîne de caractères sans les lettres 'c' et 'C'.
    :rtype: str
    """
    # Construction progressive de la nouvelle chaîne
    new_string = ""  # Affecte une valeur à 'new_string'
    for char in my_string:  # Boucle pour chaque caractère
        # Conserve le caractère s'il n'est pas 'c' ni 'C'
        if char != 'c' and char != 'C':  # Condition si
            new_string += char  # Ajoute le caractère au résultat
    # Retourne la chaîne filtrée
    return new_string  # Retourne le résultat
