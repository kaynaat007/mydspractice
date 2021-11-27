from typing import List


def util(s, i, n, is_palin):

    if i >= n:
        return [[]]

    result = []

    for j in range(i+1, n+1):

        if is_palin[i][j-1] == 1:
            r = util(s, j, n, is_palin) # [ [ "aa", b ], [ "a", "a", "b" ] ]
            for solution in r:
                solution.insert(0, s[i:j])
                result.append(solution)

    return result


def construct_palindrome_matrix(s):

    n = len(s)
    is_palin = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                is_palin[i][j] = 1

    for k in range(1, n):
        l = n - k
        j = k
        for i in range(l):
            if s[i] == s[j] and j - i + 1 == 2:
                is_palin[i][j] = 1
            elif s[i] == s[j] and is_palin[i+1][j-1] == 1:
                is_palin[i][j] = 1
            else:
                is_palin[i][j] = 0
            j += 1

    return is_palin


def partition(s: str) -> List[List[str]]:

    if not s:
        return [[]]
    is_palindrome = construct_palindrome_matrix(s)
    return util(s, 0, len(s), is_palindrome)



s = "aba"
s = 'aab'
s = 'aaab'
s = 'boob'
s = 'a'
print(construct_palindrome_matrix(s))
print(partition(s))






