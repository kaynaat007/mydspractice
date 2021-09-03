from typing import List


def util(s, left_count, right_count, n, result):

    if len(s) == 2 * n:
        result.append(s)
        return

    if left_count < n:
        util(s + '(', left_count + 1, right_count, n, result)
    if right_count < left_count:
        util(s + ')', left_count, right_count + 1, n, result)


def generateParenthesis(n: int):

    s = ''
    result = []
    util(s, 0, 0, n, result)
    return result

n = 4
print(generateParenthesis(n))

