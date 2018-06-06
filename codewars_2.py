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
# print('total: ', multiply_all(28))
