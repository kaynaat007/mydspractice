"""
Similar to coin change problem
via DP it takes time since we are deepcopying array within it
standard recursion is faster but it is still just good as 30%

W([1,2,3], T) = W(1,2,3), T-3) + W(1,2),  T

"""
from typing import List


def util(candidates, i, target, s, output):
    # Faster
    if target == 0:
        output.append(s)
        return
    if target < 0:
        return
    if i < 0:
        return
    alpha = s.copy()
    beta = s.copy()
    if target - candidates[i] >= 0:
        alpha.append(candidates[i])
    util(candidates, i, target-candidates[i], alpha, output)
    util(candidates, i-1, target, beta, output)
    return

def combinationSum(candidates: List[int], target: int):

    s = []
    output = []
    util(candidates, len(candidates)-1, target, s, output)
    return output


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])

from copy import copy, deepcopy


def combinationSumDp(candidates: List[int], target: int):
    # Slower due to deepcopy

    n = len(candidates)
    output = [[0 for j in range(target+1)] for i in range(n)]
    m = len(output[0])

    for i in range(n):
        for j in range(m):
            if j == 0:
                output[i][j] = []

    for i in range(n):
        cand = candidates[i]
        for j in range(1, m):
            ans = [None]
            # case 1 chose ith candidate then look for output[i][j-cand]
            if j - cand >= 0:
                last = output[i][j-cand]
                # no solution, empty array solution, proper solution
                if len(last) == 1 and last[0] is None:
                     pass
                elif len(last) == 0:
                    ans = [[cand]]
                else:
                    ans = deepcopy(last)
                    for e in ans:
                        e.append(cand)

            # case 2 do not chose ith candidate, look into output[i-1][j]
            if i-1 >= 0:
                last = output[i-1][j]
                if len(last) == 1 and last[0] is None:
                    pass
                elif len(last) == 0:
                    ans = []
                else:
                    last = deepcopy(last)
                    for e in last:
                        if len(ans) == 1 and ans[0] is None:
                            ans = [e]
                        else:
                            ans.append(e)
            output[i][j] = ans

    ans = output[n-1][target]
    if ans[0] is None:
        return []
    return ans



c = [2, 3]
t = 6

c = [2, 3, 6, 7]
t = 7

# c = [2, 3, 5]
# t = 8
#

#
c = [2]
t = 1


c = [1]
t = 1


c = [1]
t = 2


# print(combinationSum(c, t))
print(combinationSumDp(c, t))





