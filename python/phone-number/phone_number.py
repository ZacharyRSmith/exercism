class Phone(object):
    """
    (NXX)-NXX-XXXX

    where `N` is any digit from 2 through 9
    and `X` is any digit from 0 through 9.
    """
    def __init__(self, phone_number):
        ds = [d for d in phone_number if d.isnumeric()]
        if len(ds) == 11 and ds[0] == '1':
            ds = ds[1:]
        if len(ds) != 10:
            raise ValueError('msg')
        if int(ds[0]) not in range(2, 10):
            raise ValueError(f'The first number must be 2-9 but saw "{ds[0]}"')
        if int(ds[3]) not in range(2, 10):
            raise ValueError(f'The fourth number must be 2-9 but saw "{ds[0]}"')
        self._number = ''.join(ds)

    @property
    def area_code(self):
        return self._number[0:3]

    @property
    def exchange_code(self):
        return self._number[3:6]

    @property
    def number(self):
        return self._number

    @property
    def subscriber_number(self):
        return self._number[6:]

    def pretty(self):
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'
