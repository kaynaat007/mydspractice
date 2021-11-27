from typing import List


def arraySign(nums: List[int]) -> int:

    prod = 1
    for e in nums:
        prod = prod * e
    if prod > 0:
        return 1
    elif prod == 0:
        return 0
    return -1

# nums = [-1,-2,-3,-4,3,2,1]
# nums = [1,5,0,2,-3]
# nums = [-1,1,-1,1,-1]
# print(arraySign(nums))


def findTheWinner(n: int, k: int) -> int:

    mark = {}
    for i in range(n):
        mark[i] = 1
    i = 0
    size = n
    print(mark)
    while n-1:

        if i + k - 1 <= size-1:
            l = i + k - 1
        else:
            l = (i + k - 1) % size
        print('deleting: {}'.format(l))
        del mark[l]
        n -= 1
        i = (l + 1) % size
    print(mark)
    for i in range(size):
        if mark[i] == 0:
            return i + 1

n = 5
k = 2
print(findTheWinner(n, k))
