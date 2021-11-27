from typing import List


def util(arr, i, k, n, single, result):

    if k == 0:
        result.append(single.copy())
        return
    for j in range(i, n):
        single.append(arr[j]) # chose
        util(arr, j+1, k-1, n, single, result) # explore
        single.remove(arr[j])  # unchose


def combine(n: int, k: int) -> List[List[int]]:

    arr = []
    for i in range(n):
        arr.append(i+1)
    single = []
    result = []
    util(arr, 0, k, n, single, result)
    return result


n = 20
k = 20
print(combine(n, k))






