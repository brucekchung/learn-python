#Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.


def dashatize(num):
    num_str = str(num)
    for i in ['1','3','5','7','9']:
        num_str = num_str.replace(i,'-' + i + '-')
    return num_str.strip('-').replace('--','-')

print('1234: ', dashatize('1234'))


