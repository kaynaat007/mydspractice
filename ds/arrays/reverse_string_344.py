from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    i = 0
    n = len(s)
    j = n-1
    if n == 0:
        return
    while i < n //2:
        t = s[i]
        s[i] = s[j]
        s[j] = t
        i += 1
        j -= 1


s = ['o', 'h', 'd', 'e', 'a', 'r']
s = ['a', 'b']
s = ['a']
s = ['a', 'b', 'c']
print(reverseString(s))
