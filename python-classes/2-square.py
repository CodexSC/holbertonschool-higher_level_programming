#!/usr/bin/python3
"""1-square module"""  # Module minimal définissant la classe Square


class Square:  # Définition de la classe 'Square'
    """A class that defines a square with size validation."""  # Docstring en anglais conservée

    def __init__(self, size=0):  # Constructeur: paramètre `size` par défaut 0

        # Vérifie que `size` est bien de type entier (`int`).
        if not isinstance(size, int):  # Si `size` n'est pas un int
            # On lève une TypeError pour indiquer le mauvais type fourni.
            raise TypeError("size must be an integer")

        # Vérifie que `size` n'est pas une valeur négative.
        if size < 0:  # Si `size` est inférieur à 0
            # On lève une ValueError pour indiquer que la taille doit être >= 0.
            raise ValueError("size must be >= 0")

        # Affecte la valeur validée à l'attribut privé `__size`.
        # Cet attribut représente la longueur du côté du carré.
        self.__size = size
