'''

binary search + soritng
n * logm + nlogn
n ( logm + logn )

binary search + heap

n * logm + n * logk

n ( logm + logk )

'''

from typing import List



def find_last_one(arr, low, high, n):

    if low > high:
        return -1

    mid = low + (high - low)//2

    if 0 <= mid < n and arr[mid] == 1:
        if mid + 1 < n and arr[mid+1] == 0 or mid + 1 >= n:
            return mid
        elif mid + 1 < n and arr[mid+1] == 1:
            return find_last_one(arr, mid+1, high, n)
    elif 0 <= mid < n:
        return find_last_one(arr, low, mid-1, n)
    else:
        return -1


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:

    if not mat:
        return []
    n = len(mat)
    m = len(mat[0])
    output = []
    for i in range(n):

        idx = find_last_one(mat[i], 0, m-1, m)
        ones = idx + 1
        output.append((i, ones))

    output = list(sorted(output, key=lambda x: (x[1], x[0])))
    return [i for i, ones in output[:k]]



arr = [1, 1, 1, 0, 0]
arr = [1, 1, 1, 1]
arr = [0, 0]

# n = len(arr)
# low = 0
# high = n - 1
# print(find_last_one(arr, low, high, n))

# mat = [[1, 1, 1, 0, 0]]
mat = [[1, 0], [1, 0]]

# mat = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
print(kWeakestRows(mat, k))




