import math

def is_square(n):
    square = math.sqrt(n)
    print('square', square)
    if isinstance(square, int):
        return True
    else:
        return False

# print(is_square(4))

#solution:
# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0;

#highest profit:
def min_max(list):
    return [min(list), max(list)]

print(min_max([1, 2, 3, 4]))

def round(n):
    if (n % 5 == 0):
        return n

print('round', round(5))

