#!/usr/bin/python3
"""Module that defines a Square class."""  # Module définissant une classe Square


class Square:  # Définit la classe 'Square'
    """Represents a square with a private size attribute."""  # Docstring conservée

    def __init__(self, size=0):  # Définit la fonction '__init__'
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Utilise le setter `size` pour réutiliser la validation existante
        self.size = size  # Affecte une valeur à 'self.size'

    @property
    def size(self):  # Getter pour la propriété size
        """Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        # Retourne la valeur privée stockée dans __size
        return self.__size  # Retourne le résultat

    @size.setter
    def size(self, value):  # Setter pour la propriété size
        """Set the size of the square.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        # Validation: `value` doit être un int
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # Validation: `value` doit être >= 0
        if value < 0:
            raise ValueError("size must be >= 0")
        # Affecte la valeur validée à l'attribut privé
        self.__size = value  # Affecte une valeur à 'self.__size'

    def area(self):  # Définit la fonction 'area'
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        # Calcule l'aire en élevant la taille au carré
        return self.__size ** 2  # Retourne le résultat
