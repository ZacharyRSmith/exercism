class Allergies (object):
    def __init__(self, allergy_score):
        # NOTE: I changed self.list to the pythonic self.lst
        self.lst = self._set_lst(allergy_score)

    def is_allergic_to(self, allergen):
        return allergen in self.lst

    def _set_lst(self, allergy_score):
        lst = []
        allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128,
        }

        for a, score in allergens.iteritems():
            if score & allergy_score > 0:
                lst.append(a)

        return lst
