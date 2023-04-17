#!/usr/bin/python3

"""Define a class square"""
class square:
    """for the square"""
    def __init__(self, size=0):
        """
        Args:
            size(int): the default size is 0.

        Raises:
            TypeError: if size is an integer.
            ValueError: if size is not >= 0.
        """
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns: area of the square"""
            return(self.__size ** 2)    
