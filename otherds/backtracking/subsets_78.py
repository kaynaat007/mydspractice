from typing import List
from copy import copy


def util(selection_list):

    """
    result = []
    def backtrack(Path, Seletion List):
        if meet the End Conditon:
            result.add(Path)
            return

        for seletion in Seletion List:
            select
            backtrack(Path, Seletion List)
            deselect
    """

    if not selection_list:
        return [[]]

    selection = selection_list[0]
    selection_list.remove(selection)  # O(n)
    subsets = util(selection_list)
    new_subsets = []
    for e in subsets:
        new_subsets.append(e)
        x = copy(e)  # O(n)
        x.append(selection)
        new_subsets.append(x)
    return new_subsets


def subsets_v1_backtracking(nums: List[int]):

    return util(nums)


def subsets_v2_incremental_method(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    for n in nums:
        for i in range(len(res)):
            res.append(res[i] + [n])
    return res


def subsets_v3_bitmagic(nums):

    result = []
    n = len(nums)
    if n == 0:
        return [[]]
    for v in range(2 << n-1):
        k = len(nums) - 1
        ans = []
        while v:
            if v & 1:
                ans.append(nums[k])
            k = k-1
            v = v >> 1
        result.append(ans)
    return result


def subsets_v4(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res


def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i + 1, path + [nums[i]], res)


nums = [1,2, 3]
# nums = []
# print(subsets(nums))
# print(subsets_v2_incremental_method(nums))
# nums = [1,2]
# nums = [1, 2, 3, 4]
# nums = []
# nums = [1,1]
# print(subsets_v3_bitmagic(nums))
# print(subsets_v1_backtracking(nums))
print(subsets_v4(nums))

