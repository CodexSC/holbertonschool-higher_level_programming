#!/usr/bin/python3

# Tente d'imprimer un entier et renvoie True si réussi, False sinon
def safe_print_integer(value):  # Définit la fonction 'safe_print_integer'
    """Imprime la valeur formatée comme entier et retourne True si l'impression réussit.

    Si la valeur n'est pas convertible en entier (TypeError/ValueError), retourne False.
    """
    try:  # Tente de formater et d'imprimer la valeur
        print("{:d}".format(value))  # Affiche à l'écran
        return True  # Succès
    except (TypeError, ValueError):  # Si la conversion échoue
        return False  # Échec
