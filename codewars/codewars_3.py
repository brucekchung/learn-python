#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s):
    lower_case = s.lower()
    x = 0
    o = 0
    for i in lower_case:
        if i == 'x':
            x += 1
        if i == 'o':
            o += 1
    return (x == o)

print('true: ', xo('xxoo'))
print('false: ', xo('xoo'))

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

