

class Integer():
    def __init__(self, value):
        print(type(value) == int)
        if(type(value) == int):
            self.value = value
        else:
            raise TypeError('value is not number')
        pass

class Complex():
    def __init__(self):
        pass

class Matrix():
    
    def __init__(self, col, row, matrixList):
        self.col = col
        self.row = row
        self.matrixList = matrixList
        pass


    @staticmethod
    def make_unit_matrix(n):
        return
        
    @staticmethod
    def get_ith_row(matrix, i):
        return

    @staticmethod
    def get_ith_col(matrix, i):
        return

    @staticmethod
    def  is_zero_matrix(matrix):
        return

    @staticmethod
    def  is_unit_matrix(matrix):
        return

    @staticmethod
    def  is_bottom_triangular_matrix(matrix):
        return

    @classmethod
    def  make_matrix_from_string(elements):
        return


x = Integer(2)