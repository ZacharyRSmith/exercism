def difference(num):
    return square_of_sum(num) - sum_of_squares(num)

def square_of_sum(num):
    return sum(range(1, num + 1))**2

def sum_of_squares(num):
    return reduce((lambda x, y: x + y**2), range(1, num+1))
