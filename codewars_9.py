#Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1


print('next square: ', find_next_square(121))
print('121: ', math.sqrt(121))

