#Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer

def solution(n):
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

    # return hundreds[int(n / 100)] + tens[int(n / 10)] + ones[n % 10]
    return hundreds[int(n / 100)] + ones[n % 10]


# print('5: ', solution(5))
# print('69: ', solution(69))
print('113: ', solution(113))


