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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
