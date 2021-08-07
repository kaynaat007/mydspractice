from typing import List


def is_palindrome(array):

    n = len(array)
    for i in range(n//2):
        if array[i] != array[n-i-1]:
            return False
    return True


def util(s, k, n, current, output):
    """

    """
    if k >= n:
        output.append(current.copy())
        return
    for i in range(k, n):
        left_str = s[k:i+1]
        print(left_str)
        if left_str and is_palindrome(left_str):
            # print('checked ')
            current.append(left_str)
            util(s, i + 1, n, current, output)
            current.pop()


def partition(s: str) -> List[List[str]]:
    k = 0
    current = []
    output = []
    n = len(s)
    util(s, k, n, current, output)
    return output

s = 'ab'
s = 'aa'
s = 'aab'
s = 'abc'
s = 'a'
s = "dqsfsfsdaaaabc"
s = "cbbbcc"
"""

[
["c","b","b","b","c","c"],
["c","b","b","b","cc"],
["c","b","bb","c","c"],
["c","b","bb","cc"],
["c","bb","b","c","c"],
["c","bb","b","cc"],
["c","bbb","c","c"],
["c","bbb","cc"],
["cbbbc","c"]]
"""
print(partition(s))




