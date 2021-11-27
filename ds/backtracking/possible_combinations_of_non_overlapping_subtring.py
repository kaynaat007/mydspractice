"""
https://www.techiedelight.com/break-string-non-overlapping-substrings/

Input: ABC
Output:
{ABC}
{AB} {C}
{A} {BC}
{A} {B} {C}

"""


def util(k,  target,  n,  path, output):
    if k == n:
        output.append(path.copy())
        return

    for i in range(k, n):
        path.append(target[k:i+1])
        util(i+1, target, n, path, output)
        path.pop()


def print_possible_combinations(target):
    """

    """
    output = []
    path = []
    n = len(target)
    util(0, target, n, path, output)
    return output


Target = 'ABCD'
print(print_possible_combinations(Target))

