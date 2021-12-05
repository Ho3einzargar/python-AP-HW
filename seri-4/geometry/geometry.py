from abc import abstractmethod


class Shape:
 
    def noofsides(self):
        pass


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
