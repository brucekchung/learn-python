print('hello world')
print("let's see how quotes work")

#math operation tests
print(4 % 2)
print(5 % 2)

#variables
cars = 100
space_in_a_car = 4.0
drivers = 30

print('number of cars is', cars)
print(f'number of cars is {cars}')

hilarious = False
joke_evaluation = 'isnt the joke funny!? {}'

print(joke_evaluation.format(hilarious))

w = 'left side..'
e = 'right side'
print(w + e)

formatter = '{} {} {} {}'
print(formatter.format(1, 2, 3, 4))

# print('how old are you',
# age = input())

name = input('what is your name? ')
print('hello, %s' %name)
