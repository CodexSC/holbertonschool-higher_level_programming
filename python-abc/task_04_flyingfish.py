#!/usr/bin/python3
"""Module démontrant l'héritage multiple avec Fish, Bird et FlyingFish."""


class Fish:
    """Classe simple décrivant un poisson."""

    def swim(self):
        """Affiche que le poisson est en train de nager."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat typique du poisson."""
        print("The fish lives in water")


class Bird:
    """Classe simple décrivant un oiseau."""

    def fly(self):
        """Affiche que l'oiseau est en train de voler."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat typique de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Poisson volant : combine les comportements de Fish et Bird."""

    def fly(self):
        """Redéfinit le comportement de vol pour le FlyingFish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Redéfinit le comportement de natation pour le FlyingFish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Explique que cette créature peut vivre dans l'eau et l'air."""
        print("The flying fish lives both in water and the sky!")
