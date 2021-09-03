from typing import List
from copy import copy


def util(path, selection_list, result):
    """
    :param path: current path
    :param selection_list:  what remains in selection list
    :param result: output

    Standard approach here
    path and selection list are containers throughout the call stack.
    There memory doesn't change.
    standard way basically does a selection, then a recursive call, then deselection.
    Had to ask QA on stackoverflow to understand iteration concept.

    NOTE:
    calling path.pop() in deselection took a long time to figure out.
    subtle bug if we call path.remove(e) instead since
    say path is [2,1,1] and SL = [2]
    we updated path with [2,1,1,2] and SL = []
    but when recursion ends and we at deselection, if we do path.remove(2), it will remove first 2 from path
    leading to [1,1,2]. This is wrong path. it should be [2,1,1] only. basically whatever was before recursion call
    HENCE we do path.pop()
    """

    if len(selection_list) == 0:
        result.append(copy(path))
        return

    prev = None
    for index, selection in enumerate(selection_list):

        if prev is not None and selection == prev:
            continue

        prev = selection

        path.append(selection)
        selection_list.remove(selection)
        util(path, selection_list, result)
        path.pop()
        selection_list.insert(index, selection)

    return "RETURNING"


def util_v2(path, selection_list, result):

    """
    :param path: current path
    :param selection_list: what remains in selection list
    :param result: output
    :return:

    variant of original version where we were deselecting the path and selection list.
    Here deselection is not required  because after return of the recursive call, nothing is modified of the path
    and selection list which was sent. This is because we are giving a new memory each time when we call
    recursive util().
    """

    if len(selection_list) == 0:
        result.append(path)
        return

    for index in range(len(selection_list)):

        if index > 0 and selection_list[index] == selection_list[index-1]:
            continue

        path = path + [selection_list[index]] # for a new path with prev path and new element
        selection_list = selection_list[:index] + selection_list[index+1:]  #
        # select everything except what is at index i
        util(path, selection_list, result)

    return "RETURNING"



def permute(nums: List[int]) -> List[List[int]]:

    path = []
    result = []
    nums = sorted(nums)
    selection_list = [e for e in nums]
    util(path, selection_list, result)
    return result

def permute_v2(nums: List[int]) -> List[List[int]]:

    path = []
    result = []
    nums = sorted(nums)
    selection_list = [e for e in nums]
    util(path, selection_list, result)
    return result


from collections import Counter


"""
todo: check out this approach 
"""
def permute_v3_counter_approach(nums):

    def btrack(path, counter):
        if len(path)==len(nums):
            ans.append(path[:])
        for x in counter:  # dont pick duplicates
            if counter[x] > 0:
                path.append(x)
                counter[x] -= 1
                btrack(path, counter)
                path.pop()
                counter[x] += 1
    ans = []
    btrack([], Counter(nums))
    return ans


nums = [1,2,3]
nums = []
nums = [1]

nums = [1,1,2]
nums = [1,2,3]
nums = [1,1,1]

nums = [1,1,2,2]
nums = [1,1,2]
# nums = [1]

# nums = [0, 0]
# nums = [0,1,0,0,9]

print(permute(nums))
print(permute_v2(nums))
print(permute_v3_counter_approach(nums))

# print(permuteUnique(nums))
#
# def f(e):
#     for x in e:
#         # e.remove(1)
#         #f(e)
#         e.append(1)
#         print(x)
#
# e = [1]
# f(e)


result = []


