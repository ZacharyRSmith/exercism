import re
import numpy as np


class Matrix(object):

    def __init__(self, matrix_string):
        self.rows = [[int(num) for num in re.split(r'\D+', r)]
                     for r in matrix_string.splitlines()]
        self.columns = np.array(self.rows).T.tolist()
        # If you don't want to use numpy:
        # self.columns = [list(column) for column in zip(*self.rows)]
