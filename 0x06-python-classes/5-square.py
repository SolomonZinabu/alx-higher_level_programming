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
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Properties for the length of a sise of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function for private attribute size
            Args:
                value: value to be set.
            Returns:
                nothing.
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
=======
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
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

    def my_print(self):
        """Prints the square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
=======
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
