"""
Reverse a number.
check overflow.
"""

def reverse(x: int) -> int:
    negative = False
    if x < 0:
        negative = True
        x = abs(x)
    z = x
    rev = 0
    positive_limit = (1 << 31) - 1
    negative_limit = -1 * (1 << 31)
    while z:
        d = z % 10
        z = z // 10
        rev = rev * 10 + d
        if negative and rev * -1 < negative_limit:
            return 0
        if (not negative) and rev > positive_limit:
            return 0

    if negative:
        return -1 * rev
    return rev

# n = 2147483648
n = 1463847412

n = 123

n = -123
print(reverse(n))