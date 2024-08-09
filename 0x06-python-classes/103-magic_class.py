#!/usr/bin/python3
"""
MagicClass module.

This module defines the MagicClass which models a circle with methods to
calculate the area and circumference based on a given radius.
"""

import math


class MagicClass:
    """
    Class representing a circle with radius and methods to compute its area
    and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass instance.

        Args:
        radius (int or float): The radius of the circle. Must be a number.
        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
