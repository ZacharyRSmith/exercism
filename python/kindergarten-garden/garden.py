#!/usr/bin/env python3

"""Includes data and a Class for a kindergarten's garden."""

PLANTS = {
    'C': 'Clover',
    'G': 'Grass',
    'R': 'Radishes',
    'V': 'Violets'
}
STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph',
            'Kincaid', 'Larry']


class Garden(object):
    """Class representing a kindergarten's garden.

    Given @rows, can tell you which plants each child in the kindergarten class
    is responsible for.
    """

    def __init__(self, rows, students=STUDENTS):
        """
        Sets self.garden_map.

        @type rows: string
        @param rows: plants from left-to-right.
        Rows are separated by `\n`.
        Starts with the row nearest the windows.
        Letters represent

        @type students: string
        @param students: students whose plants are in this garden.
        """
        row_0, row_1 = rows.split()

        def student_plants(i):
            return [PLANTS[key] for key in row_0[i:i + 2] + row_1[i:i + 2]]
        plants = [student_plants(student_idx)
                  for student_idx in range(0, len(row_0), 2)]
        self.garden_map = dict(zip(sorted(students), plants))

    def plants(self, student):
        """Returns the plants planted by @student."""
        return self.garden_map[student]
