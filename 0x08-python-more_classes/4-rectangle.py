#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains a definition for class rectangle.
"""


class Rectangle:
    """Definition of class rectangle.

       Attributes:
           width(int): rectangle width.
           height(int): rectangle height.
    """
    def __init__(self, width=0, height=0):
        """
            Initializes a new Class Rectangle instance.

            Args:
                width(int): rectangle width.
                height(int): rectangle height.

            Raises:
                TypeError: if width/height is not int.
                ValueError: if width/ height is not >= 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
            getter function for private attribute width.
            Returns: width of the rectangle.
        """
=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """
            setter function for private attribute width.
            Args:
                value(int) new width value.
            Raises:
                TypeError: if value is not int.
                ValueError: if value is not >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
=======
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """
            getter function for private attribute height.
            Returns: height of the triangle.
        """
=======
        """Get/set the height of the Rectangle."""
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        """
            setter function for private attribute height.
            Args:
                value(int) new width value.
            Raises:
                TypeError: if value is not int.
                ValueError: if value is not >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method to compute area of rectangle.
           Returns: area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method to compute perimeter of triangle.
           Returns: perimeter of triangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns string representation of a rectangle.
        """
        rect = []
        if self.__height == 0 or self.__width == 0:
            return ""
        for n in range(0, self.__height):
            rect.append("#" * self.__width)
            if n != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)

    def __repr__(self):
        """Return string representation of rectangle.
            Should be able to create a new instance using eval().
        """

        return '{self.__class__.__name__}({self.width}, {self.height})'.\
            format(self=self)
=======
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
