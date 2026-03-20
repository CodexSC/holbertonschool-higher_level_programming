#!/usr/bin/python3
"""Module démontrant des mixins : SwimMixin, FlyMixin et la classe Dragon."""


class SwimMixin:
    """Mixin fournissant la capacité de nager."""

    def swim(self):
        """Affiche que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin fournissant la capacité de voler."""

    def fly(self):
        """Affiche que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon combinant nage et vol via l'utilisation de mixins."""

    def roar(self):
        """Affiche le rugissement du dragon."""
        print("The dragon roars!")
