"""

when strings are equal characterwise

check if frequency of any character is more than 1. if it is, you can swap those two characters

when a and b are not equal characterwise

so in this case, find the first point of difference say x and y
now check if you can get y in a and x in b after this point of difference.

if you can get this exactly 1 time, means you can do swap.

"""

from collections import Counter
def buddyStrings(A: str, B: str) -> bool:

    n1 = len(A)
    n2 = len(B)

    if n1 == 0:
        return False
    if n2 == 0:
        return False
    if A == B:
        freq = Counter(A)
        return len(list(filter(lambda y: y > 1, freq.values()))) > 0

    if (n1 < n2) or (n2 < n1):
        return False

    i = 0
    j = 0
    count = 0
    next_x = None
    next_y = None

    while i < n1 and j < n2:
         x = A[i]
         y = B[j]

         if next_x and next_y and x == next_x and y == next_y:
             print(next_x, next_y)
             count += 1

         if x != y:
            next_x = y
            next_y = x

         i += 1
         j += 1

    if count == 1:
        return True
    return False

a = 'ab'
b = 'ba'

# a = 'ab'
# b = 'ab'
#
# a = 'aa'
# b = 'aa'

# a = 'aaaaaaabc'
# b  = 'aaaaaaacb'

# a = ""
# b = "aa"
#
# a = "abcaa"
# b = "abcbb"

# a = 'abc'
# b = 'acb'

a = "abab"
b = "abab"

a = 'abc'
b = 'abc'


print(buddyStrings(a, b))

