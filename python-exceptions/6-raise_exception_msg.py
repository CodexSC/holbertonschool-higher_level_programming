#!/usr/bin/python3

# Fonction qui lève une NameError avec un message fourni
def raise_exception_msg(message=""):  # Définit la fonction 'raise_exception_msg'
    """Lève une NameError en utilisant `message` comme message d'erreur."""
    raise NameError(message)  # Code