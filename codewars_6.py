#Write a function that takes an array and counts the number of each unique element present.

from collections import Counter

def count(array):
    return Counter(array)

print('count: ', count(['a', 'a', 'b']))
