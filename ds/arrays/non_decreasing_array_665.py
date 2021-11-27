from typing import List


def checkPossibility(nums: List[int]) -> bool:

    n = len(nums)
    if n == 0:
        return True
    if n == 1:
        return True

    count = 0

    if nums[0] > nums[1]:
        nums[0] = nums[1]
        count += 1

    prev = nums[0]

    for i in range(1, n-1):

        if nums[i] > nums[i+1]:
            if nums[i + 1] >= prev:
                nums[i] = nums[i + 1]
            else:
                nums[i+1] = nums[i]
            count += 1
        if count > 1:
            return False
        prev = nums[i]

    # print(nums)

    return True


nums = [1,2,3]

nums = [4,2,3]

nums = [4,2,1]

nums = [2, 2, 1]

nums = [2, 2, 2]

nums = [2, 2, 1, 3, 4]

nums =[2, 2, 1, 3, 4, 1]

nums =[2, 2, -100, 1]

nums = [-1, 4, 2, 3]

nums = [3, 8, 4]

nums = [2, 1]
print(checkPossibility(nums))

