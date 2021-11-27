from typing import List

'''

Not possible to remove duplicates by this approach since each element can
occur > 1 in given input 
so count of indexes > 1 for such elements. 

While looking into the map for target T, it's uncertain on how to find index idx such tha idx > j. 


'''
def threeSum(nums: List[int]) -> List[List[int]]:

    output = set()
    n = len(nums)
    store = {}
    for i, e in enumerate(nums):
        if e not in store:
            store[e] = [i]
        else:
            store[e].append(i)

    for i in range(n-2):
        for j in range(i+1, n-1):
            target = -1 * (nums[i] + nums[j])
            if target in store:
                    # indexes = store[target]
                    # for idx in indexes:
                    #     if idx > j:
                    #
                    output.add(tuple(sorted([nums[i], nums[j], target])))
    return output


nums = [-1,0,1,2,-1,-4]
nums = [1,3,2,2,-4]

# { -1 : [0, 4], 0: [1], 1: [2], 2: [3], -4: [5] }
#
nums = [1,2,-2,-1]
print(threeSum(nums))

