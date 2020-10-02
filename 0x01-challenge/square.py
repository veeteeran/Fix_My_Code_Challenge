#!/usr/bin/python3

class rectangle():
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """Init for square """
        for key, value in kwargs.items():
            setattr(self, key, value)

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

    def area_of_my_rectangle(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMyRectangle(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = rectangle(width=12, height=9)
    print(s)
    print(s.area_of_my_rectangle())
    print(s.PermiterOfMyRectangle())
