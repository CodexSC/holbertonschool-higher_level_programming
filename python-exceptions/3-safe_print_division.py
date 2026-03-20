#!/usr/bin/python3

# Effectue une division en toute sécurité et affiche le résultat à l'intérieur d'un message
def safe_print_division(a, b):  # Définit la fonction 'safe_print_division'
    """Tente de diviser `a` par `b`, affiche le résultat (ou None) et retourne la valeur.

    Si `b` est 0, attrape ZeroDivisionError et retourne None.
    """
    try:  # Tente la division
        result = a / b  # Affecte une valeur à 'result'
    except ZeroDivisionError:  # Division par zéro
        result = None  # Attribue None pour signaler l'erreur
    finally:  # Bloc exécuté quoi qu'il arrive
        print("Inside result: {}".format(result))  # Affiche le résultat (ou None)
    return result  # Retourne le résultat
