class Allergies(object):
    def __init__(self, score: int) -> None:
        allergens = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats'
        }
        self.lst = [a for k, a in allergens.items() if k & score]

    def is_allergic_to(self, allergen: str) -> bool:
        return allergen in self.lst
