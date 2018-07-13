# We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

# So given a string "super", we should return a list of [2, 4].

def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']

print('vowel index: ', vowel_indices('hello'))
