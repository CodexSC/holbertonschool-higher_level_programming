#!/usr/bin/python3
"""Module définissant une classe Shape abstraite et des implémentations concrètes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite représentant une forme géométrique.

    Les sous-classes doivent implémenter `area` et `perimeter`.
    """

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre."""
        pass


class Circle(Shape):
    """Cercle : implémente area et perimeter."""

    def __init__(self, radius):
        """Initialise un cercle en s'assurant d'un rayon positif."""
        # On prend la valeur absolue pour garantir un rayon non négatif
        self.radius = abs(radius)

    def area(self):
        """Calcule l'aire du cercle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule la circonférence."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle : implémente area et perimeter."""

    def __init__(self, width, height):
        """Initialise un rectangle avec largeur et hauteur."""
        self.width = width
        self.height = height

    def area(self):
        """Calcule l'aire (width * height)."""
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre (2*(width + height))."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'un objet suivant le principe duck-typing.

    L'objet `shape` doit exposer les méthodes `area()` et `perimeter()`.
    """
    # Appelle les méthodes sur l'objet fourni sans vérifier son type explicitement
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
