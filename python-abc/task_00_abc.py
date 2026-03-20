#!/usr/bin/python3
"""Module définissant une classe abstraite Animal et ses sous-classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite de base pour les animaux.

    Les classes dérivées doivent implémenter la méthode `sound`.
    """

    @abstractmethod
    def sound(self):
        """Méthode abstraite devant retourner le son de l'animal.

        Doit être implémentée par les sous-classes concrètes.
        """
        pass  # Placeholder pour la méthode abstraite


class Dog(Animal):
    """Classe représentant un chien héritant de Animal."""

    def sound(self):
        """Retourne le son produit par un chien (ex: Bark)."""
        # Implémentation concrète pour la sous-classe Dog
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat héritant de Animal."""

    def sound(self):
        """Retourne le son produit par un chat (ex: Meow)."""
        # Implémentation concrète pour la sous-classe Cat
        return "Meow"
