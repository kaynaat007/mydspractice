"""

gap representation of ALGORITHM and  ALTRUISTIC. gap representation means when we have a gap in first row, we inserted
a character , when we have a gap in second row, we deleted a character from first row. Columns with two different
characters correspond to replacement.

minimum number of operations needed to transform ALGORITHM into ALTRUISTIC is number of columns which do not contain
same character twice.

A L G O R   I   T H M
A L   T R U I S T I C

minimum operations:  6 for G -- empty ( del ), o -- T ( replace ), empty -- U ( insertion ) ,
empty -- S ( insert ), H --I ( replace ) , M --- C ( replace ).

optimal substructure

    This representation has an optimal substructure property. Our original problem involves finding minimum distance between
    X[1..m] Y[1..n]. Means if we look at last columns, and if we remove them, then remaining columns must represent the shortest
    edit sequence for the remaining prefixes.

    claim:

    Assume we take k steps which is minimum to transform original strings X[1..i]
    to Y[1..j].
    if we remove last column, transformation of remaining prefixes X[1..i-1] and Y[1..j-1] must be optimal.

    proof:

    Assume there is some shorter other shorter way having z < s  steps to transform X[1..i-1] to Y[1..j-1], where s is minimum steps for
    transformation of X[1..i-1] to Y[1..j-1].  z < s<=k.  We add last column transformation to this then
    we achieve an even shorter way to transform X[1...i] to Y[1...j] in less than k steps  which
    is a contradiction. so z == s.


recursive formulation for optimal value:

    Let E(i, j) be the optimal distance of string X[1..i] and Y[1..j]. Remember, here we are looking at prefix of
    X and Y to calculate edit distance.

    Three things can happen to the last characters of X[1..i] and Y[1..j].

    Goal is to reduce our main problem into solving sub-problems
    INSERTION

    say we add a character c equal to Y[j] at the last of X[1..i]. This means we have done the job of achieving the transformation
    of X[i+1] to Y[j]. Now problem reduces by 1 in Y, but remains same in X.
    so we say
    E(i, j) = 1 + E(i, j-1)

    Deletion

    say we delete the last char of X[1..i]. We are left with problem size -1 in X, but the problem is same in Y. at j.
    so we have E(i, j) = 1 + E(i-1, j)


    Replacement

    say the last two chars are different, we replace the X[i] with Y[j] and we solve for problem size - 1 in both X and Y.
    E(i, j) = 1 + E(i-1, j-1) if X[i] != Y[j]

    if last two chars are same, the transformation is free so we have

    E(i, j) = E(i-1, j-1) if last two chars are same.


    also we need to consider the fact that when either of the string is empty, cost is length of the other string.
    E(i, j) = 0 if i == 0 and j == 0. Transformation of an empty string to empty is free.

    by combining all these we can come with a recursive formulation to calculate optimal value

    E(i, j) =  min ( 1 + E(i, j-1),
                     1 + E(i-1, j),
                     1 + E(i-1, j-1) if X[i] != Y[j],
                     E(i-1, j-1) if X[i] == Y[j],
                     i if j == 0,
                     j if i == 0
                )


Compute the value of optimal solution:

    Let E[m][n] be a matrix in which cell E(i, j) will represent min steps to transform string X[1..i] to Y[1...j].

    E(i, j) = i  for all j = 0
    E(i, j) = j for all i = 0

    we shall take bottom up approach. for a cell value of E(i, j), we need E(i-1, j), E(i-1, j-1), E(i, j-1). so we
    can fill the matrix in row major order. answer will be E(m-1, n-1).


"""


def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def edit_distance(w1, w2):
    m = len(w1)
    n = len(w2)
    c = [[0 for __ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        c[i][0] = i
    for i in range(n+1):
        c[0][i] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if w1[i-1] == w2[j-1]:
                c[i][j] = c[i-1][j-1]
            else:
                c[i][j] = min(1 + c[i][j-1], 1 + c[i-1][j], 1 + c[i-1][j-1])
    return c


w1 = 'ALGORITHM'
w2 = 'ALTRUISTIC'

# w1 = 'horse'
# w2 = 'ros'

# w1 = 'intention'
# w2 = 'execution'

c = edit_distance(w1, w2)
print_matrix(c)


