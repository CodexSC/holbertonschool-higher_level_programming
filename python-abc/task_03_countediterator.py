#!/usr/bin/python3
"""Module définissant CountedIterator qui compte les éléments itérés."""


class CountedIterator:
    """Wrapper d'itérateur qui conserve un compteur d'itérations."""

    def __init__(self, iterable):
        """Initialise l'itérateur interne et le compteur.

        Args:
            iterable: objet itérable à envelopper.
        """
        # Convertit l'itérable en itérateur et initialise le compteur
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Retourne l'objet itérateur lui-même (nécessaire pour `for` loops)."""
        return self

    def __next__(self):
        """Renvoie l'élément suivant et incrémente le compteur d'itérations.

        Lève StopIteration lorsque l'itérateur est épuisé.
        """
        item = next(self._iterator)  # Récupère l'élément suivant
        self._count += 1  # Incrémente le compteur
        return item

    def get_count(self):
        """Retourne le nombre d'éléments déjà itérés.

        Returns:
            int: compteur actuel d'itérations.
        """
        return self._count
