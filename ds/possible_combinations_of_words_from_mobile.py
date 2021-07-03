

def util(i, mat,  n, ans, result):
    if i == n:
        result.append(ans)
        return

    for j in range(n):
        util(i+1, mat, n, ans + mat[i][j], result)


def possible(nums):

    str1 = ['A', 'B', 'C']
    str2 = ['D', 'E', 'F']
    str3 = ['G', 'H', 'I']
    i = 0
    mat = []
    mat.append(str1)
    mat.append(str2)
    mat.append(str3)
    result = []
    ans = ""
    n = len(nums)
    print(mat)
    util(i, mat, n, ans, result)
    return result

nums = [2, 3, 4]
print(possible(nums))

