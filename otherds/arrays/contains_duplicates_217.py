from typing import List

def containsDuplicate(nums: List[int]) -> bool:

    return len(nums) != len(set(nums))


def containsDuplicateV2(nums: List[int]) -> bool:

    hash = {}
    for e in nums:
        if e in hash:
            return True
        else:
            hash[e] = True
    return False

nums =  [1,2,3,1]
print(containsDuplicateV2(nums))

nums = [1,2,3,4]
print(containsDuplicateV2(nums))

