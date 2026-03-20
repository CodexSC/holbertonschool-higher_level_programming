#!/usr/bin/python3
"""Module that defines a Square class."""  # Module définissant une classe Square


class Square:  # Définit la classe 'Square'
    """A class that represents a square."""  # Docstring conservée

    def __init__(self, size=0):  # Définit la fonction '__init__'
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Utilise le setter pour appliquer la validation
        self.size = size  # Affecte une valeur à 'self.size'

    @property
    def size(self):  # Getter de la propriété size
        """Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        # Retourne la valeur privée __size
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
        # Validation de type et de valeur
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        # Affecte la valeur validée
        self.__size = value  # Affecte une valeur à 'self.__size'

    def area(self):  # Définit la fonction 'area'
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        # Calcule et retourne l'aire
        return self.__size**2  # Retourne le résultat

    def my_print(self):  # Définit la fonction 'my_print'
        """Print the square using the # character.

        If size is 0, prints an empty line.
        """
        # Si la taille est 0, on imprime simplement une ligne vide
        if self.__size == 0:
            print()
        else:
            # Pour chaque ligne, on imprime une chaîne composée de '#'
            for _ in range(self.__size):
                print("#" * self.__size)  # Affiche à l'écran
