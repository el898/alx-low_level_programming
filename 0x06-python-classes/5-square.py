#!/usr/bin/python3

""" Represents a square class"""

class square:
    """for the square"""

    def __init__(self,size=0)
    """
    initialize a square instance.
     
    Args:
        size(int): The default size is 0.
    """
    self.size = size

    @property
    def size(self):
        """
        getter: gets the current value of the square
        """
        return (self.size = size)

    @size.setter
    def size(self, value):
         if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
