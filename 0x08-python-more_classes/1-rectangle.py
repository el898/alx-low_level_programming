#!/usr/bin/python3

""" Creates a rectangle class"""


class rectangle:
    """a rectangle"""

    def __init__(self, width=0, height=0):
    
    """intialize a rectangle
    Args:
        width(int): width of the new triangle.
        height(int): heigth of the new triangle.
    """
    self.width = width
    self.height = height

    @property
    def width(self):
        """gets the current width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the current width."""
        if not isinstance(width,int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """gets the current height"""
        return( self.__height)

    @height.setter(self,value):
        """sets the height"""
        if not isinstance(height,int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
