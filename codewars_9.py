#Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

import math

def find_next_square(sq):
    root = sq ** 0.5  #note ** vs *
    if root.is_integer():  #is_integer() is float method
        return (root + 1)**2
    return -1

print('next square: ', find_next_square(121))

