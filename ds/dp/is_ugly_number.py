"""

if number is not divisible by 2,3,5 it is not an ugly number.
else
if we eliminate all the 2,3,5 factors from input n, we can conclude that if number remaining is 1, it is ugly number
else it is not.
"""

def is_ugly(n):

    if n == 1:
        return True

    if n <= 0:
        return False

    v1 = n % 2 == 0
    v2 = n % 3 == 0
    v3 = n % 5 == 0

    if (not v1) and (not v2) and (not v3):
        return False

    while n%2 == 0:
        n = n / 2

    while n% 3 == 0:
        n = n /3

    while n%5 == 0:
        n = n/5

    if n == 1:
        return True
    return False

n =  19
print(is_ugly(n))
