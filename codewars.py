#return sum of 1 through input 'n'

def sumOfRange(n):
    return sum(range(1, n)) 

print('sumOfRange: ', sumOfRange(10))



#return total time needed to queue given the customers and tills

def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)

#print a diamond shape out - must have 1 at top and bottom
#input n must be middle/thickest row, adjacent rows are -2 width



#find unique number in arr, think about performance
    
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


#write algorithm to id valid IP address ie 123.45.67.89 (0 - 255)

def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4


