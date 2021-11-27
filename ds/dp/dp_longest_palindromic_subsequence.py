"""
Longest palindromic subsequence

optimal substructure:

LPS of a string X[1..m] depends on LPS of substring X[2..m-1] if X[0] == X[m]. which means if first and last
two characters match, problem reduces to finding LPS of X[2..m-1]. So we are left with 1 subproblem if the condition matches.
This subproblem must be optimal. That is X[2..m-1] must also be LPS of X[2...m-1].

if X[0] != X[m], then LPS will come from either X[1..m-1] or X[2..m]. need to take max on both.

optimal solution to main problem contains optimal solutions to subproblems.


recursive way to calculate optimal value:

Let lps[i, j] means length of longest palindromic subsequence of string X[i..j].

lps(i, j) = 0 if  i == 0 and j == 0
lps(i, j) = 2 + lps(i+1, j-1) if X[i] == X[j]
lps(i, j) = max(lps(i, j-1), lps(i+1, j) if X[i] != X[j]


computation of optimal value:

we shall take bottom up approach.

"""


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


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


s = 'cbbd'
n = len(s)
c = lps(s)
print(print_matrix(c))
print(c[0][n-1])







