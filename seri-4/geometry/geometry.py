from abc import abstractmethod


class Shape:

    def get_area(self):
        pass
        return

    def get_perimeter(self):
        pass
        return

    def __str__(self):
        pass
        return


    @classmethod
    def check_if_args_not_below_zero(cls,*args):
        for arg in args:
            if arg < 0:
                raise ValueError
        return True        

    @classmethod
    def get_area_formula(cls):
        return

    @classmethod
    def get_perimeter_formula(cls):
        return  


class Circle(Shape):

    def __init__(self, r):
        self.check_if_args_not_below_zero(r)
        self.r = r

    def get_area(self):
        return super().get_area()

    @abstractmethod
    def get_area(self):
        pass
        return

    @abstractmethod
    def get_perimeter(self):
        pass
        return

    @abstractmethod
    def __str__(self):
        pass
        return




class Triangle(Shape):
    def __init__(self, a, b, c):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.check_if_args_not_below_zero(c)
        self.a = a
        self.b = b
        self.c = c

class Rectangle(Shape):
    def __init__(self, a, b):
        self.check_if_args_not_below_zero(a)
        self.check_if_args_not_below_zero(b)
        self.a = a
        self.b = b
class Square(Rectangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
class RegularPantagon(Shape):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        self.check_if_args_not_below_zero(a)
        self.a = a





class ShapeList():
        
    def add_shape(self, shape):
        self.Shape.append(shape);
    def get_shapes_table(self):
        return self.shape;
    def get_largest_shape_by_perimeter(self):
        return 
    def get_largest_shape_by_area(self):
        return
