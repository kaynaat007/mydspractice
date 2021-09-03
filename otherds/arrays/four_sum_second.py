from typing import List


def two_sum(array1, array2, target):

    output = []
    n = len(array1)
    i = 0
    j = n-1
    while i < n and j >= 0:
        curr_sum = array1[i] + array2[j]
        if curr_sum < target:
            i += 1
        elif curr_sum > target:
            j -= 1
        else:
            output.append((array1[i], array2[j]))
            i += 1
            j -= 1
    return output


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int])->int:

    A = sorted(A)
    B = sorted(B)
    C = sorted(C)
    D = sorted(D)

    n = len(A)
    result = []
    for i in range(n):
        for j in range(n):
            remaining_target = -1 * (A[i] + B[j])
            remaining_indexes = two_sum(C, D, remaining_target)
            for a, b in remaining_indexes:
                result.append((A[i], B[j], C[a], D[b]))
    return len(result)

A = [3, 6, 7, 9]
B = [1, 2, 3, 4]

print(two_sum(A, B, 10))


#
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [0, 2]
#
#
# A = [-1,-1]
# B = [-1,1]
# C = [-1,1]
# D = [1,-1]
#
#
# A = [0,1,-1]
# B = [-1,1,0]
# C = [0,0,1]
# D = [-1,1,1]
#
# print(fourSumCount(A, B, C, D))




