class EAST (object):
    pass

class NORTH (object):
    pass

class SOUTH (object):
    pass

class WEST (object):
    pass

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot (object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        if self.bearing == NORTH:
            self._add_y(1)
        elif self.bearing == EAST:
            self._add_x(1)
        elif self.bearing == SOUTH:
            self._add_y(-1)
        elif self.bearing == WEST:
            self._add_x(-1)

    def simulate(self, arg):
        for ltr in arg:
            if ltr == "L":
                self.turn_left()
            elif ltr == "R":
                self.turn_right()
            elif ltr == "A":
                self.advance()

    def turn_left(self):
        crnt_idx = DIRECTIONS.index(self.bearing)
        next_idx = (len(DIRECTIONS) - 1 if crnt_idx == 0 else crnt_idx - 1)

        self.bearing = DIRECTIONS[next_idx]

    def turn_right(self):
        crnt_idx = DIRECTIONS.index(self.bearing)
        next_idx = (0 if crnt_idx == len(DIRECTIONS) - 1 else crnt_idx + 1)

        self.bearing = DIRECTIONS[next_idx]

    # PRIVATE METHODS

    def _add_x(self, n):
        lst = list(self.coordinates)
        lst[0] += n
        self.coordinates = tuple(lst)

    def _add_y(self, n):
        lst = list(self.coordinates)
        lst[1] += n
        self.coordinates = tuple(lst)
