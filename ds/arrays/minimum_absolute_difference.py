from typing import List
import math


def b_search_pre_sorted_array(arr, low, high, target, n):

    """
    returns an index i, after which  target should be inserted.
    """
    #
    if low == high: # case for 1
        return low

    if low + 1 == high: # case for 2

        if target >= arr[high]:
            return high
        else:
            return low

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if target == arr[mid] and mid + 1 < n and target != arr[mid+1]:
        return mid
    elif mid + 1 < n and arr[mid] < target < arr[mid+1]:
        return mid
    elif target >= arr[mid]:
        return b_search_pre_sorted_array(arr, mid+1, high, target, n)
    else:
        return b_search_pre_sorted_array(arr, low, mid-1, target, n)


def minAbsoluteSumDiff(nums1: List[int], nums2: List[int]) -> int:
    """

    :param nums1:
    :param nums2:
    :return:

    A = sort num1 in  decreasing order with index
    B = sort abs(num1-num2) and pick the highest one. Let the cooresponding num2 be b
    A' = modify A such that each element in A is abs(A[i] - b)
    search min value in A'. This corresponds to optimum A[i] such that A[i] - b is minimum
    subtract from total sum - A[i] - b
    """
    num1 = nums1
    num2 = nums2
    MOD = pow(10, 9) + 7
    n = len(nums1)
    if n == 1:
        return abs(num1[0] - num2[0])

    total = 0
    for i in range(n):
        total += (abs(num1[i] - num2[i])) % MOD

    _total = 0
    for i in range(n):
        _total += (abs(num1[i] - num2[i]))

    # print('total: {},{}'.format(total, _total))
    min_sum = total
    pre_sorted_array_num1 = []

    for i in range(n):
        pre_sorted_array_num1.append(num1[i])

    pre_sorted_array_num1 = sorted(pre_sorted_array_num1)

    print('sorted: {}'.format(pre_sorted_array_num1))
    # target = 97
    # index = b_search_pre_sorted_array(pre_sorted_array_num1, 0, n - 1, target, n)
    # print('index : {}, e = {}'.format(index, pre_sorted_array_num1[index]))
    #

    max_adj_sum = -1 * math.inf

    for i in range(n):

        target = num2[i]

        index = b_search_pre_sorted_array(pre_sorted_array_num1, 0, n-1, target, n)

        if index != -1:
            if index == n-1:
                closest_element = pre_sorted_array_num1[index]
            else:
                if abs(target - pre_sorted_array_num1[index]) < abs(target - pre_sorted_array_num1[index+1]):
                    closest_element = pre_sorted_array_num1[index]
                else:
                    closest_element = pre_sorted_array_num1[index+1]

            print('closest element for num2[i] {} is  num1[k]: {}, index from b search: {}'.format(target, closest_element, index))

            adjusted_sum = abs(num1[i] - num2[i]) - abs(closest_element - num2[i])
            if adjusted_sum > max_adj_sum:
                max_adj_sum = adjusted_sum
            min_sum = min(min_sum, (total - adjusted_sum))

    # print('max adj sum: {}'.format(max_adj_sum))
    # print('max adj sum closest index: {}'.format(max_adj_sum_closest_index))
    return min_sum % MOD

num1 = [1, 7, 5]
num2 = [2, 3, 5]
#
# num1 = [1,10,4,4,2,7]
# num2 = [9,3,5,1,7,4]

# #
num1 = [2,4,6,8,10]
num2 = [2,4,6,8,10]
# #
# # num1 = [10]
# # num2 = [3]
# #
# num1 = [10, 20]
# num2 = [20, 10]
#
# num1 = [8, 9, 10, 11, 12]
# num2 = [7, 3, 9, 22, 10]

num1 = [57,42,21,28,30,25,22,12,55,3,47,18,43,29,20,44,59,9,43,7,8,5,42,53,99,34,37,88,87,62,38,68,31,3,11,61,93,34,63,27,20,48,38,5,71,100,88,54,52,15,98,59,74,26,81,38,11,44,25,69,79,81,51,85,59,84,83,99,31,47,31,23,83,70,82,79,86,31,50,17,11,100,55,15,98,11,90,16,46,89,34,33,57,53,82,34,25,70,5,1]
num2 = [76,3,5,29,18,53,55,79,30,33,87,3,56,93,40,80,9,91,71,38,35,78,32,58,77,41,63,5,21,67,21,84,52,80,65,38,62,99,80,13,59,94,21,61,43,82,29,97,31,24,95,52,90,92,37,26,65,89,90,32,27,3,42,47,93,25,14,5,39,85,89,7,74,38,12,46,40,25,51,2,19,8,21,62,58,29,32,77,62,9,74,98,10,55,25,62,48,48,24,21]


# num1 = [53,48,14,71,31,55,6,80,28,19,15,40,7,21,69,15,5,42,86,15,11,54,44,62,9,100,2,26,81,87,87,18,45,29,46,100,20,87,49,86,14,74,74,52,52,60,8,25,21,96,7,90,91,42,32,34,55,20,66,36,64,67,44,51,4,46,25,57,84,23,10,84,99,33,51,28,59,88,50,41,59,69,59,65,78,50,78,50,39,91,44,78,90,83,55,5,74,96,77,46]
# num2 = [39,49,64,34,80,26,44,3,92,46,27,88,73,55,66,10,4,72,19,37,40,49,40,58,82,32,36,91,62,21,68,65,66,55,44,24,78,56,12,79,38,53,36,90,40,73,92,14,73,89,28,53,52,46,84,47,51,31,53,22,24,14,83,75,97,87,66,42,45,98,29,82,41,36,57,95,100,2,71,34,43,50,66,52,6,43,94,71,93,61,28,84,7,79,23,48,39,27,48,79]

#
# num1 =  [1,2,3,4,5]
# num2 = [1,4,3,9,1000]

print(minAbsoluteSumDiff(num1, num2))






