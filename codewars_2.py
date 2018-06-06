#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.


def persistence(n, counter = 0):
    if (len(str(n)) > 1):
        counter += 1
        new_sum = multiply_all(n)
        return persistence(new_sum, counter)
    else:
        return counter
    
def multiply_all(input):
    total = 1
    string = str(input)
    for i in string:
        total *= int(float(i))
    return total



print('solution: ', persistence(999))


#codewars solutions:

import operator
def persistence_1(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

def persistence_2(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

