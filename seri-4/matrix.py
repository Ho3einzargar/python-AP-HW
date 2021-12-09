class Integer():
    """

        |----------------------------------------------------------
        |                                                         |
        |     Integer Class                                       |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial Integer class and check type of value     |
        |                                                         |
        -----------------------------------------------------------

    """

    # -> 1
    def __init__(self, value):
        if(type(value) == int):
            self.value = value
        else:
            raise TypeError('value is not number')
        pass

class Complex():

    """

        |----------------------------------------------------------
        |                                                         |
        |     Complex Class -> its note complete!                 |
        |                                                         |
        |----------------------------------------------------------


    """

    def __init__(self):
        pass

class Matrix():

    """

        |----------------------------------------------------------
        |                                                         |
        |     Matrix Class                                        |
        |                                                         |
        |----------------------------------------------------------
        |                                                         |
        |   1 - initial Matrix class bt row & col count & matrix  |
        |                                                         |
        |   2 -  make unit matrix                                 |
        |                                                         |
        |   3 -  get specefic row                                 |
        |                                                         |
        |   4 -  get specefic col                                 |
        |                                                         |
        |   5 -  check matrix is zero matrix                      |
        |                                                         |
        |   6 -  check matrix is unit matrix                      |
        |                                                         |
        |   7 -  check matrix is bottom triangular matrix         |
        |                                                         |
        |   8 -  check matrix is top triangular matrix            |
        |                                                         |
        |   9 -  make matrix from string                          |
        |                                                         |
        -----------------------------------------------------------

    """
    # -> 1    
    def __init__(self, col, row, matrixList):
        self.col = col
        self.row = row
        self.matrixList = matrixList
        pass

    # -> 2
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
  
    # -> 3 
    @staticmethod
    def get_ith_row(matrix, i):
        return  matrix[i]
  
    # -> 4
    @staticmethod
    def get_ith_col(matrix, i):
        col = []
        for j in matrix:
            col.append(j[i])
        print(col)
        return col
  
    # -> 5
    @staticmethod
    def  is_zero_matrix(matrix):
        for row in matrix:
            for col in row:
                if col != 0:
                    return False
        return  True
 
    # -> 6
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
 
    # -> 7
    # TODO: most implement
    @staticmethod
    def  is_bottom_triangular_matrix(matrix):
        return

    # -> 8
    # TODO: most implement
    @staticmethod
    def  is_top_triangular_matrix(matrix):
        return

    # -> 9
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