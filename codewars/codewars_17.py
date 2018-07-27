# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.



def maskify(cc):
    last_4 = cc[-4:]
    total_masked = len(cc) - 4
    masked = ''
    for i in range(total_masked):
        masked += '#'
    return masked + last_4

print('brucechung: ', maskify('brucechung'))

#alternate solution:

# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]
