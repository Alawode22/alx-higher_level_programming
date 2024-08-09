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
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            row = '#' * self.__size
        print('\n'.join([row] * self.__size))
