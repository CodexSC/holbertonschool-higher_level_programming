#!/usr/bin/python3

# Retourne un tuple (longueur de la chaîne, premier caractère)
def multiple_returns(sentence):  # Définit la fonction 'multiple_returns'
    """Retourne un tuple contenant la longueur de la chaîne et son premier caractère.

    :param sentence: La chaîne à analyser.
    :type sentence: str

    :return: Un tuple (longueur, premier_caractère). Si la chaîne est vide, le premier caractère est `None`.
    :rtype: tuple
    """
    # Calcule et stocke la longueur de la chaîne
    length = len(sentence)  # Affecte une valeur à 'length'

    # Récupère le premier caractère si existant, sinon None
    first = sentence[0] if length > 0 else None  # Affecte une valeur à 'first'

    # Retourne les deux valeurs dans un tuple
    return (length, first)  # Retourne le résultat
