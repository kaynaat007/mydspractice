from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:

    low = 0
    high = len(numbers) - 1
    n = len(numbers)

    while 0 <= low < high < n:
        curr = numbers[low] + numbers[high]
        if curr < target:
            low += 1
        elif curr > target:
            high -= 1
        else:
            return [low + 1, high + 1]



numbers = [2,7,11,15]
target = 9

numbers =  [2,3,4]
target = 6

numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))


