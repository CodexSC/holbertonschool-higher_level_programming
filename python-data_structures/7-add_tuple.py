#!/usr/bin/python3

# Additionne deux tuples (élément par élément) et retourne un tuple de longueur 2
def add_tuple(tuple_a=(), tuple_b=()):  # Définit la fonction 'add_tuple'
    """Ajoute deux tuples d'entiers de longueur 2, en additionnant les éléments correspondants.

    Si un tuple a moins de deux éléments, l'élément manquant est considéré comme 0.

    :param tuple_a: Le premier tuple à ajouter. Par défaut, un tuple vide.
    :type tuple_a: tuple

    :param tuple_b: Le deuxième tuple à ajouter. Par défaut, un tuple vide.
    :type tuple_b: tuple

    :return: Un nouveau tuple contenant les sommes des éléments correspondants de `tuple_a` et `tuple_b`.
    :rtype: tuple
    """
    # Récupère le premier élément ou 0 si absent
    first_a = tuple_a[0] if len(tuple_a) > 0 else 0  # Affecte une valeur à 'first_a'
    first_b = tuple_b[0] if len(tuple_b) > 0 else 0  # Affecte une valeur à 'first_b'

    # Récupère le second élément ou 0 si absent
    second_a = tuple_a[1] if len(tuple_a) > 1 else 0  # Affecte une valeur à 'second_a'
    second_b = tuple_b[1] if len(tuple_b) > 1 else 0  # Affecte une valeur à 'second_b'

    # Retourne le tuple avec les sommes correspondantes
    return (first_a + first_b, second_a + second_b)  # Retourne le résultat
