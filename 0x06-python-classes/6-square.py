#!/usr/bin/python3
"""Module that defines a Square class with size and position attributes."""

class Square:
    """Class that represents a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position.
        
        Args:
            size (int): The size of the square, must be a non-negative integer.
            position (tuple): A tuple of 2 positive integers that indicates the position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, ensuring it is a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or 
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character '#'.
        
        The square will be printed with spaces according to its position attribute.
        If the size is 0, an empty line will be printed.
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
