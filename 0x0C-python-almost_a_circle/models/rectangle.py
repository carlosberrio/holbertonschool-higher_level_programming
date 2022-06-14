#!/usr/bin/python3
"""
...
"""


from models.base import Base


class Rectangle(Base):
    """
    ...
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """...
        """
        return self.__width

    @width.setter
    def width(self, value):
        """...
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """...
        """
        return self.__height

    @height.setter
    def height(self, value):
        """...
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """...
        """
        return self.__x

    @x.setter
    def x(self, value):
        """...
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """...
        """
        return self.__y

    @y.setter
    def y(self, value):
        """...
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        ...
        """
        return self.__width * self.__height

    def __str__(self):
        """
        ...
        """
        return str(f"[Rectangle] ({self.id}) {self.__x}/" +
                   f"{self.__y} - {self.__width}/{self.__height}")

    def display(self):
        """display: prints in stdout the Rectangle instance
        with the character #
        """
        for row in range(self.y):
            print("")
        for col in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """
        ...
        """
        if args is not None and len(args) > 0:
            if type(args[0]) is not int and args[0] is not None:
                raise ValueError
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for k, value in kwargs.items():
                if k == "id":
                    self.id = value
                if k == "width":
                    self.__width = value
                if k == "height":
                    self.__height = value
                if k == "x":
                    self.__x = value
                if k == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        ...
        """
        my_dictionary = {"id": self.id, "width": self.__width,
                         "height": self.__height, "x": self.__x, "y": self.__y}
        return my_dictionary
