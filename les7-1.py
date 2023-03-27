class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        for row in self.matrix:
            matrix_str += ' '.join(str(x) for x in row) + '\n'
        return matrix_str

matrix = Matrix([[3, 5, 32], [2, 4, 6], [8, 3, 7]])
print(matrix)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        max_len = 0
        for row in self.matrix:
            for item in row:
                if len(str(item)) > max_len:
                    max_len = len(str(item))
        for row in self.matrix:
            matrix_str += ' '.join(str(x).ljust(max_len) for x in row) + '\n'
        return matrix_str

matrix = Matrix([[3, 5, 32], [2, 4, 6], [8, 3, 7]])
print(matrix)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        max_len = 0
        for row in self.matrix:
            for item in row:
                if len(str(item)) > max_len:
                    max_len = len(str(item))
        for row in self.matrix:
            matrix_str += ' '.join(str(x).ljust(max_len) for x in row) + '\n'
        return matrix_str

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

matrix_1 = Matrix([[3, 5, 32], [2, 4, 6], [8, 3, 7]])
matrix_2 = Matrix([[31, 32, 3], [37, 43, 2], [51, 86, -1]])
print(matrix_1 + matrix_2)