import re


class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = [re.split(r'\D+', r) for r in matrix_string.split('\n')]
        for i in range(len(self.rows)):
            self.rows[i] = [int(num) for num in self.rows[i]]
        self.columns = [list(column) for column in zip(*self.rows)]
