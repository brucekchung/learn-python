# thing = 'asdf'
# print('test %s')%thing

def print_one(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# print_one('guy', 'stuff')

def add(first, second): 
    return first + second

def test(first, second):
    print(add(first, second))

test(2, 2)

numbers = [1, 2, 3, 3, 4, 5]

# for i in numbers: 
#     print(i)

for i in range(0, 11):
    print(i)

print('hello' * 10)
