from typing import  List
from math import ceil


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    if n == 0:
        return True
    k = len(flowerbed)
    if k == 1 and flowerbed[0] == 0 and n == 1:
        return True
    if k == 1 and flowerbed[0] == 1 and n > 0:
        return False

    slow = 0
    fast = 0
    t = 0
    s = 0
    while slow <= fast < k:
        while slow < k and flowerbed[slow] == 1:
            slow += 1
            fast += 1
        count = 0
        while fast < k and flowerbed[fast] == 0:
            fast += 1
            count += 1
        print(count)
        if count and slow == 0 and flowerbed[slow] == 0:
            t = t + ceil((count-1)/2)
        elif count and fast - 1 == k-1 and flowerbed[fast - 1] == 0:
            t = t + ceil((count-1)/2)
        elif count:
            t = t + ceil((count - 2)/2)
        slow = fast
        if t >= n:
            return True
        s = s + count

    if s == k:
        return ceil(k / 2) >= n
    return t >= n

flowers = [1, 0, 0, 0, 1]
n = 2

# flowers = [0, 0, 0]

# flowers = [0, 0 , 1]
# n = 2

# flowers = [1, 0, 0, 0, 1, 0, 0]
# n = 3


# flowers = [0, 0, 1, 0, 0, 0]
# n = 3

# flowers = [1, 1, 1, 1]
# n = 1

flowers = [1,0,0,0,0,1]
n = 2

flowers = [1, 0, 0, 0, 0]
n = 3

flowers = [0]
n = 1

flowers = [1]
n = 2

flowers = [0, 1]
n = 1

flowers =[0, 1, 0]
n = 1

flowers = [0, 0, 0]
n = 2

# flowers = [0, 0, 0, 0]
# n = 3

print( canPlaceFlowers(flowers, n))
