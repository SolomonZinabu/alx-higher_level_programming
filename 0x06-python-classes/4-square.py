#!/usr/bin/python3
<<<<<<< HEAD
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Properties for the length of a sise of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size
=======
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
<<<<<<< HEAD
        if value < 0:
=======
        elif value < 0:
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
<<<<<<< HEAD
        """Area of the square.

        Returns:
            thee size squared.
        """
        return self.__size ** 2
=======
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
