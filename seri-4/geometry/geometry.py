from abc import abstractmethod


class Shape:

    """

        |--------------------------------------------------
        |                                                 |
        |     Shape abstract Class                        |
        |                                                 |
        |--------------------------------------------------
        |                                                 |
        |   1 - get area of shape                         |
        |                                                 |
        |                                                 |
        |   2 - get perimeter of shape                    |
        |                                                 |
        |   3 - get info of shape                         |
        |                                                 |
        |   4 - check argumat not below zero              |
        |                                                 |
        |   5 - get shape perimeter formula               |
        |                                                 |
        |   6 - get shape area formula                    |
        |                                                 |
        ---------------------------------------------------

    """

    # -> 1
    def get_area(self):
        pass
        return

    # -> 2
    def get_perimeter(self):
        pass
        return

    # -> 3
    def __str__(self):
        pass
        return

    # -> 4
    @classmethod
    def check_if_args_not_below_zero(cls,*args):
        for arg in args:
            if arg < 0:
                raise ValueError
        return True        
    # -> 5
    @classmethod
    def get_area_formula(cls):
        return
    # -> 6
    @classmethod
    def get_perimeter_formula(cls):
        return  


class Circle(Shape):

    
    """

        |----------------------------------------------------------
        |                                                         |
        |     Circle Class                                        |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial circle class                              |
        |                                                         |
        |   2 - implement abstract method: get area of shape      |
        |                                                         |
        |                                                         |
        |   3 - implement abstract method: get perimeter of shape |
        |                                                         |
        |   4 - implement abstract method: info of shape          |
        |                                                         |
        -----------------------------------------------------------

    """
    # -> 1
    def __init__(self, r):
        self.check_if_args_not_below_zero(r)
        self.r = r

    # -> 2
    @abstractmethod
    def get_area(self):
        return int(self.r) * int(self.r) * 3.14;
    # -> 3
    @abstractmethod
    def get_perimeter(self):
        return  2 * int(self.r) * 3.14;
    # -> 4
    @abstractmethod
    def __str__(self):
        return 'circle r is' , self.r


class Triangle(Shape):
    """

        |----------------------------------------------------------
        |                                                         |
        |     Triangle Class                                      |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial Triangle class                            |
        |                                                         |
        |   2 - implement abstract method: get area of shape      |
        |                                                         |
        |                                                         |
        |   3 - implement abstract method: get perimeter of shape |
        |                                                         |
        |   4 - implement abstract method: info of shape          |
        |                                                         |
        ------------------------------------------------------------

    """
    # -> 1
    def __init__(self, a, b, c):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.check_if_args_not_below_zero(c)
        self.a = a
        self.b = b
        self.c = c

    # -> 2
    @abstractmethod
    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return pow(s * (s - self.a) * (s - self.b) * (s - self.c), 0.5);
    # -> 3
    @abstractmethod
    def get_perimeter(self):
        return  self.a + self.b + self.c
    # -> 4
    @abstractmethod
    def __str__(self):
        return 'circle sides is' , self.a , self.b, self.c

class Rectangle(Shape):

    """

        |----------------------------------------------------------
        |                                                         |
        |     Rectangle Class                                     |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial Rectangle class                           |
        |                                                         |
        |   2 - implement abstract method: get area of shape      |
        |                                                         |
        |                                                         |
        |   3 - implement abstract method: get perimeter of shape |
        |                                                         |
        |   4 - implement abstract method: info of shape          |
        |                                                         |
        ------------------------------------------------------------

    """

    # -> 1    
    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.a = a
        self.b = b
    # -> 2
    @abstractmethod
    def get_area(self):
        return self.a * self.b;
    # -> 3
    @abstractmethod
    def get_perimeter(self):
        return 2 * (self.a + self.b);
    # -> 4
    @abstractmethod
    def __str__(self):
        return 'circle sides is' , self.a , self.b;
class Square(Rectangle):
    """

        |----------------------------------------------------------
        |                                                         |
        |     Square Class                                        |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial Square class base on Rectangle class      |
        |                                                         |
        -----------------------------------------------------------

    """
    # -> 1
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a

    # ? dont need implement abstract method
class RegularPantagon(Shape):

    """

        |----------------------------------------------------------
        |                                                         |
        |     RegularPantagon Class                               |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial RegularPantagon class                     |
        |                                                         |
        |   2 - implement abstract method: get area of shape      |
        |                                                         |
        |                                                         |
        |   3 - implement abstract method: get perimeter of shape |
        |                                                         |
        |   4 - implement abstract method: info of shape          |
        |                                                         |
        ------------------------------------------------------------

    """
    # -> 1
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
        self.c = a
    # -> 2
    @abstractmethod
    def get_area(self):
        return 0.25 * pow(5 * (5 + 2 * pow(5, 0.5)), 0.5) * self.a * self.a;
    # -> 3
    @abstractmethod
    def get_perimeter(self):
        return  self.a * 5
    # -> 4
    @abstractmethod
    def __str__(self):
        return 'circle side is' , self.a

class EquilateralTriangle(Triangle):

    """

        |----------------------------------------------------------
        |                                                         |
        |     EquilateralTriangle Class                                        |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial EquilateralTriangle class base on Triangle class      |
        |                                                         |
        -----------------------------------------------------------

    """

    # -> 1
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
        self.b = a
        self.c = a
    # ? dont need implement abstract method

class ShapeList():

    """

        |----------------------------------------------------------
        |                                                         |
        |     ShapeList Class                                     |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - add shape to list                                 |
        |                                                         |
        |   2 - get all shape list                                |
        |                                                         |
        |                                                         |
        |   3 - get largest shape by perimeter                    |
        |                                                         |
        |   4 - get largest shape by area                         |
        |                                                         |
        ------------------------------------------------------------

    """
    # -> 1
    def add_shape(self, shape):
        self.Shape.append(shape);
    # -> 2
    def get_shapes_table(self):
        return self.shape;
    # -> 3
    def get_largest_shape_by_perimeter(self):
        return 
    # -> 4
    def get_largest_shape_by_area(self):
        return
