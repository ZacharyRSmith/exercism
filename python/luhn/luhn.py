import copy


class Luhn(object):
    def __init__(self, card_num):
        self.card_num_list = [int(i) for i in str(card_num)]

    def addends(self):
        lst = copy.copy(self.card_num_list)
        for i in range(len(self.card_num_list) - 2, -1, -2):
            lst[i] *= 2
            if lst[i] > 10:
                lst[i] -= 9

        return lst

    def checksum(self):
        return sum(self.addends()) % 10

    @staticmethod
    def create(num):
        # Brute force it
        for i in range(10):
            newNum = int(str(num) + str(i))
            if Luhn(newNum).is_valid():
                return newNum

    def is_valid(self):
        return self.checksum() == 0
