import math
from typing import List


def b_search(arr, target, low, high):

    if low > high:
        return low

    mid = math.floor(low + (high - low)/2)

    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return b_search(arr, target, low, mid-1)
    return b_search(arr, target, mid+1, high)


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:

    e = b_search(arr, x, 0, len(arr)-1)
    n = len(arr)
    s = []
    target = x
    x = e - 1
    y = e
    c = 0
    while c < k:
        left = None
        right = None
        if x >= 0:
            left = abs(target - arr[x])
        if y <= n-1:
            right = abs(target - arr[y])

        if left is None:
            s.append(arr[y])
            y += 1
            c += 1
        elif right is None:
            s.append(arr[x])
            x -= 1
            c += 1
        else:
           if left <= right:
                s.append(arr[x])
                x -= 1
                c += 1
           else:
                s.append(arr[y])
                y += 1
                c += 1

    return sorted(s)


arr = [1, 2, 3, 4, 50, 60]
k = 4
x = 4

arr = [0,1,1,1,2,3,6,7,8,9]

# print(b_search(arr, 1 , 0, len(arr) - 1))


# arr = [1,2,3,4,5]
# k = 4
# x = 3
#
# arr = [1, 2, 3, 4, 5]
# k = 2
# x = 20
# print(findClosestElements(arr, k, x))

arr = [0,1,1,1,2,3,6,7,8,9]
k = 3
x = 10
print(findClosestElements(arr, k, x))



