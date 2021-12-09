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
        identityMatrix = []
        for i in range(n):
            row = []    
            for j in range(n):
                row.append(0)
            row[i] = 1
            identityMatrix.append(row)

        return identityMatrix
        
    @staticmethod
    def get_ith_row(matrix, i):
        return  matrix[i]

    @staticmethod
    def get_ith_col(matrix, i):
        col = []
        for j in matrix:
            col.append(j[i])
        print(col)
        return col

    @staticmethod
    def  is_zero_matrix(matrix):
        for row in matrix:
            for col in row:
                if col != 0:
                    return False
        return  True

    @staticmethod
    def  is_unit_matrix(matrix):
        if len(matrix[0]) != len(matrix):
            return False

        for i, row in enumerate(matrix):
            if row[i] != 1:
                return False
            for col in row:
                if col != 0 and (col == row[i] and col != 1):
                    return False

        return  True

    # TODO: most implement
    @staticmethod
    def  is_bottom_triangular_matrix(matrix):
        return

    # TODO: most implement
    @staticmethod
    def  is_top_triangular_matrix(matrix):
        return

    # TODO: most implement
    @classmethod
    def  make_matrix_from_string(self, elements):
        rows = elements.split(',')
        for i ,row in enumerate(rows):
            # print(row.split(' '))
            rows[i] = row.split(' ')

        print(rows)
        return rows

# x = Matrix(2, 3, [1,2,3,4,5,6])

matrix1 = Matrix.make_matrix_from_string("1 2,3 4,5 6")


# print(x.is_unit_matrix([[1,0,0],[0,1,0],[0,0,1]]))