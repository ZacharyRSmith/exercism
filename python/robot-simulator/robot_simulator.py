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
        # t = ('275', '54000', '0.0', '5000.0', '0.0')
        # lst = list(t)
        # lst[0] = '300'
        # t = tuple(lst)
    
# class Allergies (object):
#     def __init__(self, allergy_score):
#         # NOTE: I changed self.list to the pythonic self.lst
#         self.lst = self.__gen_lst(allergy_score)

#     def is_allergic_to(self, allergen):
#         return allergen in self.lst

#     def __gen_lst(self, allergy_score):
#         allergens = {
#             1: 'eggs',
#             2: 'peanuts',
#             4: 'shellfish',
#             8: 'strawberries',
#             16: 'tomatoes',
#             32: 'chocolate',
#             64: 'pollen',
#             128: 'cats',
#         }

#         # This is part of a non-bitwise/binary solution:
# #         for score, a in sorted(allergens.iteritems(), reverse=True):
# #             if allergy_score >= score:
# #                 lst.append(a)
# #                 allergy_score -= score

#         return [allergens[score] for score in allergens.keys()
#                 if score & allergy_score > 0]

