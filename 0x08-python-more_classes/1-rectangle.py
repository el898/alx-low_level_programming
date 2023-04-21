#!/usr/bin/python3

"""Creates a rectangle class"""


class Rectangle:
    """A rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the current width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        """Get the current height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the current height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

