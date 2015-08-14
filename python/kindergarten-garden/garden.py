import operator


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
    def __init__(self, rows, students=STUDENTS):
        r0, r1 = rows.split()
        plants = [[PLANTS[key] for key in r0[i:i + 2] + r1[i:i + 2]]
                  for i in range(0, len(r0), 2)]
        self.garden_map = dict(zip(sorted(students), plants))

    def plants(self, student):
        return self.garden_map[student]
