#!/usr/bin/python3
# 1-square.py

"""square with size"""


class Square:
    """rep a square"""
    def __init__(self, size=0):
        """initialize a new square

        Args:
            size: the size of the new square
        exceptions:
            TypeError: if size is not an integer(size must be an integer)
            ValueError: if size is less than 0 (size must be >-= 0)
            """
        self.size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        if self.__size < 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)

    @property
    def size(self):
        """A getter """
        return self.__size

    @size.setter
    def size(self, value):
        """A setter attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
