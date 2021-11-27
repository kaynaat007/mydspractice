"""

example of slow pointer being catching up to fast pointer whenever certain conditions are met.

Need to reset slow pointer to fast whenever de detect either curr and prev elements are equal or
prev sign is same as current sign and curr sign ( +ve, -ve ).

window starts and registers a size of 2 at minimum if two distinct elements are there.

"""
def get_sign(a, b):
    if a == b:
        return 0
    if a > b:
        return -1
    return  1


def turbulent(A):
    slow = 0
    fast = 1
    ans = 0
    sign = None
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 1
    size = 0

    while slow < n and fast < n:

        j = fast
        new_sign = get_sign(A[j], A[j-1])
        if new_sign == 0:
            slow = j
            fast = j
            sign = None
            size = 1
        else:
            if sign is None:
                sign = new_sign
                size = 2
            else:
                if sign != new_sign:
                    size += 1
                    sign = new_sign
                else:
                    slow = j-1
                    fast = j-1
                    sign = None
                    size = 0
        ans = max(ans, size)
        fast = fast + 1
    return ans

A = []
A  = [1, 2, 1, 1, 1, 1]
# A = [4,8,12,16]
# A = [9,4,2,10,7,8,8,1,9]
# A = [5, 4, 3, 2]
# A = [1, 10, 3, 4, 2, 5]
# A = [1, 1, 1]
# A = [0,1,1,0,1,0,1,1,0,0]
print(turbulent(A))