#!/usr/bin/python3

class square():
    '''
    width = 0
    height = 0
    '''
    
    def __init__(self, width, height, **kwargs):
        """Init for square """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.width = width
            self.height = height

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method with type and value check

            Parameter:
                value: width of square
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method with type and value check

            Parameter:
                value: height of square
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        return "{}/{}".format(self.__width, self.__height)

if __name__ == "__main__":

    s = square(12, 9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
