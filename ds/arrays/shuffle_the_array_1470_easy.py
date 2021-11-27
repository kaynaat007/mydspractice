from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:

    first = 0
    second = n
    output = []

    while first < n:
        output.append(nums[first])
        output.append(nums[second])
        first += 1
        second += 1
    return output


def shuffleWithBitwise(nums: List[int], n: int) -> List[int]:

    # make pairs
    first = n-1
    second = 2 * n - 1
    k = 9
    mask = 0
    while k:
        mask = mask | 1 << k
        k = k - 1
    mask = mask | 1

    # print(mask)

    while first >= 0:
        e = nums[second]
        f = nums[first]
        e = e << 10
        e = e | f
        nums[second] = e
        second -= 1
        first -= 1

    first = 0
    second = n

    while first < 2 * n - 1:

        num1 = nums[second] & mask
        nums[second] = nums[second] >> 10
        num2 = nums[second] & mask
        nums[first] = num1
        nums[first+1] = num2
        first = first + 2
        second += 1

    return nums


nums =  [2,5,1,3,4,7]
n =  3


# nums = [1,2,3,4,4,3,2,1]
# n = 4

#
# nums = [1,1,2,2]
# n = 2
print(shuffle(nums, n))
print(shuffleWithBitwise(nums, n))



