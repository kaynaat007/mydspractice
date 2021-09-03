import math

def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def mctFromLeafValues(arr):
    """
    recurrence is .
    let c(i, j) represent minimum cost of tree considering leaves from arr[i] to arrr[j].
    then we can make a cut at any place between  i and j to divide it into subproblems c(i, k) and c(k+1, j).
    Then final cost c(i, j) = min for all k such that
        c(i, k) + c(k+1, j) + max_element(i, k) * max_element(k+1, j) for such k between i and j.

    SIMILAR TO MATRIX CHAIN MULTIPLICATION IN CLRS.

    """
    n = len(arr)

    max_mat = [ [0 for _ in range(n) ] for _ in range(n)]
    min_cost_mat = [ [0 for _ in range(n) ] for _ in range(n)]

    l = n
    k = 0
    for i in range(l):
        for j in range(k, n):
            if i == j:
                max_mat[i][j] = arr[i]
            else:
                max_mat[i][j] = max(max_mat[i][j-1], arr[j])

        k = k + 1
        l = l - 1

    for i in range(n):
        for j in range(n):
            if i == j:
                min_cost_mat[i][j] = arr[i]
            else:
                min_cost_mat[i][j] = math.inf

    gap = 0
    l = n
    for c in range(n):
        i = 0
        for d in range(l):
            j = i + gap
            for k in range(i, j):

                if i + 1 == j:
                    min_cost_mat[i][j] = arr[i] * arr[j]
                else:

                    left_subtree_cost = 0
                    right_subtree_cost = 0

                    if i != k:
                        left_subtree_cost = min_cost_mat[i][k]

                    if k + 1 != j:
                        right_subtree_cost = min_cost_mat[k+1][j]

                    min_cost_mat[i][j] = min(min_cost_mat[i][j], max_mat[i][k] * max_mat[k+1][j] + left_subtree_cost + right_subtree_cost)
            i = i + 1

        gap += 1
        l = l - 1

    return min_cost_mat[0][n-1]




# arr = [6, 2, 8, 7, 1, 4]
arr = [3,7,2,12,15,10,3,9]
#
# arr = [3,7,2,12,15,10]
# arr = [3,7,2,12,15,10, 2]
# # arr = [3, 4, 7]
# arr = [6,2,4]
arr = [10]
print(mctFromLeafValues(arr))



