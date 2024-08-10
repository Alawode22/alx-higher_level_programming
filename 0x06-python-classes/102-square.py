#!/usr/bin/python3

"""
defines an empty class
"""


class Square:
    """a square class with errors caught"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on their area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is less than another based on their area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if a square is <= to another based on the area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than another based on their area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if a square is >= to another based on the area"""
        return self.area() >= other.area()
