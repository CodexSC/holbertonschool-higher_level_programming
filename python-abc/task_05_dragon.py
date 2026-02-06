#!/usr/bin/env python3


class SwimMixin:
    """Provides swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Provides flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        print("The dragon roars!")

