def difference(num):
    return square_of_sum(num) - sum_of_squares(num)


def square_of_sum(num):
    return sum(range(num + 1))**2


def sum_of_squares(num):
    return sum(n**2 for n in range(num+1))
