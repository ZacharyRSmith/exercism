NORTH, EAST, SOUTH, WEST = range(4)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Robot (object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self._x = x
        self._y = y

    @property
    def coordinates(self):
        return (self._x, self._y)
    
    def advance(self):
        if self.bearing == NORTH:
            self._y += 1
        elif self.bearing == EAST:
            self._x += 1
        elif self.bearing == SOUTH:
            self._y -= 1
        elif self.bearing == WEST:
            self._x -= 1

    def simulate(self, instruct):
        commands = {
            'A': self.advance,
            'L': self.turn_left,
            'R': self.turn_right
        }

        for command in instruct:
            commands[command]()

    def turn_left(self):
        self.bearing = DIRECTIONS[(self.bearing - 1) % 4]

    def turn_right(self):
        self.bearing = DIRECTIONS[(self.bearing + 1) % 4]
