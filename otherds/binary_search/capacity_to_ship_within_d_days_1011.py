from typing import List


def check(capacity, arr, days, total_sum):
    """
    :param potential_answer:
    :param arr:
    :return:
    """
    sum_so_far = 0
    container = 0
    i = 0
    n = len(arr)
    while i < n:
        if container + arr[i] <= capacity:
            container += arr[i]
        else:
            days -= 1
            sum_so_far += container
            if arr[i] <= capacity:
                container = arr[i]
            else:
                container = 0
                break
        i += 1

    if container > 0:
        sum_so_far += container
        days -= 1

    # print(sum_so_far, days)
    return sum_so_far == total_sum and days >= 0


def b_search(arr, low, high, ans, days, total_sum):
    """
    stores answer in array and recurs for a better answer
    """

    if low > high:
        return

    mid = low + (high - low) // 2
    result = check(mid, arr, days, total_sum)

    if result:
        ans[0] = mid
        return b_search(arr, low, mid-1, ans, days, total_sum)
    else:
        return b_search(arr, mid+1, high, ans, days, total_sum)


def shipWithinDays(weights: List[int], D: int) -> int:
    low = 1
    high = sum(weights)
    ans = [0]
    total_sum = sum(weights)
    b_search(weights, low, high, ans, D, total_sum)
    return ans[0]


weights = [6, 2, 8]
D = 3
# total_sum = sum(weights)

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5

weights = [3,2,2,4,1,4]
D = 3
# total_sum = sum(weights)

weights = [1,2,3,1,1]
D = 4

print(shipWithinDays(weights, D))

