class Allergies (object):
    def __init__(self, allergy_score):
        # NOTE: I changed self.list to the pythonic self.lst
        self.lst = self._get_lst(allergy_score)

    def is_allergic_to(self, allergen):
        return allergen in self.lst

    def _get_lst(self, allergy_score):
        allergens = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats',
        }

        # This is part of a non-bitwise/binary solution:
#         for score, a in sorted(allergens.iteritems(), reverse=True):
#             if allergy_score >= score:
#                 lst.append(a)
#                 allergy_score -= score

        return [allergens[score] for score in allergens.keys()
                if score & allergy_score > 0]
