"""
Code intent is to show how to set variables for diagonal traversal

define d from n --- 0
    define l = n - d + 1
    define i from 0 ..... d
        set j = i + l - 1
"""


def lps(s):
    """

    """
    n  = len(s)
    if n == 0:
        return 0
    c = [ [0 for y in range(n) ] for x in range(n)]
    for d in range(n, 0, -1):
        l = n - d + 1
        for i in range(0, d):
            j = i + l - 1
            if s[i] == s[j] and i == j:
                c[i][j] = 1
            elif s[i] == s[j] and i != j:
                c[i][j] = 2 + c[i+1][j-1]
            else:
                c[i][j] = max(c[i][j-1], c[i+1][j])
    return c

