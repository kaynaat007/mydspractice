def print_matrix(k):
    for i in range(len(k)):
        print(k[i])


def dfs_util(A, i,  visited, k, target):

    if A[i] == target:
        visited[i] = True
        k = k - 1
        return
    if target <= 0:
        return

    dfs_util(A, i+1, visited, k, target - A[i])







def dp_partition_k_equal_set(A, k):

    total_sum = sum(A)
    if total_sum % k != 0:
        return False

    target = int(total_sum/k)
    n = len(A)
    visited = [False for i in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs_util(A, i, visited, k, target)
    return None


A = [4, 3, 2, 3, 5, 2, 1]
# A = [2,2,2,2,3,4,5]
# k = 4
# A = [7,2,2,2,2,2,2,2,3]
k = 4
print(dp_partition_k_equal_set(A, k))