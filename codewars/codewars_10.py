# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of theeach other; return false otherwise.


def is_anagram(test, original):
    return sorted(test.upper()) == sorted(original.upper())
#note sort vs sorted
#sort works on array/list, mutates, returns 'None'
#sorted works on str and arr, returns copy
#pass - allows block to run with no other indented code

print('true: ', is_anagram('Creative', 'Reactive'))
print('false: ', is_anagram('thing', 'stuff'))

