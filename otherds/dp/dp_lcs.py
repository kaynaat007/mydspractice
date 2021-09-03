"""

3 steps of dynammic programming


optimal substructure: LCS of two strings depends on calculating LCS of subsequences of
    the main string.

recursive way to calculate optimal value:

    let c[i,j] be length of LCS of strings Xi anx Yj. where 1<=i <=N and  1<=j<=N
    then c[i, j] = 0 if i == 0 or j == 0 since a zero length X or Y will give LCS of zero length.
    c[i,j] = 1 + c[i-1, j-1] if Xi == Yj. since X[i] == Y[j], we only need to calculate LCS
    of X[i-1] andY[j-1].
    c[i, j] = max(c[i-1, j], c[i, j-1]) if X[i] != Y[j]. This is because if X[i] != Y[j],
    there are two ways by which LCS can come.
    by calculating LCS of X[i-1] and Y[j] and by calculating LCS of X[i], Y[j-1].
    Remember, how this LCS will be calculated need not  be concerned.
    We just need to express that it is possible by comparing these two ways and
    take the max out of it. By doing this we have executed second step of
    dynammic programming which is recursive way to calculate optimal value.


Compute the optimal value : compute the optimal value using top-down with memoisation or bottom-up approach.

    top-down approach is recursion + storing of values so that we do not calculate same
    values again and again. Bottom up approach is when we calculate smaller
    size subproblems and build up upon  it to get to a bigger subproblem.
    We use size of the subproblem as a tool here.

    we will take bottom up approach here.
    solve subproblems like (0, 0), (0, 1), (0, 2) .. (0, N).
    also like (1, 0), (2, 0), (3, 0) .... (N, 0)

    Then we build up solution for c[1, 1]. This value depends on corresponding values of two strings.

"""


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 1:
        print('case 1')
        print_lcs(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j] == 2:
        print('case 2')
        print_lcs(b, X, i-1, j)
    else:
        print('case 3')
        print_lcs(b, X, i, j-1)


def lcs(text1, text2):

    m = len(text1)
    n = len(text2)
    c = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return c


if __name__ == '__main__':

    s1 = 'pmjghexybyrgzczy'
    s2 = 'hafcdqbgncrcbihkd'
    # s1 = 'abcbdab'
    # s2 = 'bdcaba'

    n1 = len(s1)
    n2 = len(s2)

    c = lcs(s1, s2)
    print(c[n1][n2])
    print_matrix(c)
    # print_matrix(b)
    # print_lcs(b, s1, len(s1)-1, len(s2)-1)
