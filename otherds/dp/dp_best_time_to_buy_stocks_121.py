

def dp_stocks(A):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 0
    last_max_diff_ending_index = 0
    max_diff_so_far = 0
    for i in range(1, n):

        current_diff_contribution = max(A[i] - A[last_max_diff_ending_index] + max_diff_so_far, A[i] - A[i-1])
        if current_diff_contribution >= max_diff_so_far:
            max_diff_so_far = current_diff_contribution
            last_max_diff_ending_index = i
        print(current_diff_contribution, max_diff_so_far)

    return max_diff_so_far


def dp_stocks_v2(A):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 0
    max_height = 0
    minimum_depth = A[0]
    for i in range(1, n):
        current_height = 0
        if A[i] > A[i-1]:
            current_height =  A[i] - A[i-1]
        else:
            minimum_depth = min(A[i], minimum_depth)
        max_height = max(max_height, current_height,  A[i] - minimum_depth)

    # print(max_height)
    return max_height


A = [4, 10, 7, 15, 20]
A = [1, 10, 7, 15, 20]
A = [4, 3, 2, 7, 1, 9]
A = [7, 1, 5, 3, 6, 4]
A = [1,  100, 1000]
A = [100, 0, 0, 0]
A = [2, 1, 2, 1, 0, 1, 2]
A = [2, 7, 1, 4, 11]
print(dp_stocks_v2(A))
