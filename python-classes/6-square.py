#!/usr/bin/python3
"""Module that defines a Square class with size and position attributes."""  # Module


class Square:  # Définit la classe 'Square'
    """A class that defines a square by its size and position.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position offset for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):  # Définit la fonction '__init__'
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides. Defaults to 0.
            position (tuple): A tuple of 2 positive integers. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        # Utilise les setters pour appliquer la validation centralisée
        self.size = size  # Affecte une valeur à 'self.size'
        self.position = position  # Affecte une valeur à 'self.position'

    @property
    def size(self):  # Getter de la propriété size
        """Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        # Retourne la valeur interne __size
        return self.__size  # Retourne le résultat

    @size.setter
    def size(self, value):  # Setter de la propriété size
        """Set the size of the square.

        Args:
            value (int): The new size of the square's sides.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        # Validation du type et de la valeur
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        # Affecte la valeur validée
        self.__size = value  # Affecte une valeur à 'self.__size'

    @property
    def position(self):  # Getter de la propriété position
        """Get the position of the square.

        Returns:
            tuple: The position offset for printing.
        """
        # Retourne la valeur interne __position
        return self.__position  # Retourne le résultat

    @position.setter
    def position(self, value):  # Setter de la propriété position
        """Set the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        # Validation : doit être un tuple de deux entiers >= 0
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        # Affecte la valeur validée
        self.__position = value  # Affecte une valeur à 'self.__position'

    def area(self):  # Définit la fonction 'area'
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        # Calcule l'aire (taille au carré)
        return self.__size ** 2  # Retourne le résultat

    def my_print(self):  # Définit la fonction 'my_print'
        """Print the square with the character # at the specified position.

        If size is 0, prints an empty line.
        Position is used to add vertical and horizontal spacing.
        """
        # Si la taille est 0, imprime une ligne vide et quitte
        if self.__size == 0:
            print()
            return

        # Imprime des lignes vides pour le décalage vertical (position[1])
        for _ in range(self.__position[1]):
            print()

        # Pour chaque ligne du carré, imprime les espaces horizontaux puis les '#'
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)  # Affiche à l'écran
