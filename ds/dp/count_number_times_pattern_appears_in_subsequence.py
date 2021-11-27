
def util(k, j, text_length, pattern_length, text, pattern, ans):

    if j == pattern_length:
        ans[0] += 1
        return

    if k >= text_length:
        return 0

    for i in range(k, text_length):
        if text[i] == pattern[j]:
            # import pdb
            # pdb.set_trace()
            util(i+1, j+1, text_length, pattern_length, text, pattern, ans)


def function(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    k = 0
    j = 0
    ans = [0]
    util(k, j, text_length, pattern_length, text, pattern, ans)
    return ans[0]


def util_2(i, j, text, pattern, ans):
    if j < 0:
        ans[0] += 1
        return 0
    if i < 0:
        return 0

    if text[i] == pattern[j]:
        util_2(i-1, j-1, text, pattern, ans)
        util_2(i-1, j, text, pattern, ans)
    else:
        util_2(i-1, j, text, pattern, ans)


def bottom_up(text, pattern):
    """
    from recursive to bottom up dp.

    w(i,j)  = w(i-1, j-1) + w(i, j-1) if pattern[i] == text(j)
    w(i, j) = w(i, j-1) if pattern(i) != text(j)
    w(i,j) = pattern * text
    """
    n = len(text)
    m = len(pattern)
    w = [[0 for _ in range(n)] for _ in range(m)]

    if text[0] == pattern[0]:
        w[0][0] = 1

    for i in range(1, n):
        if pattern[0] == text[i]:
            w[0][i] = 1 + w[0][i-1]
        else:
            w[0][i] = w[0][i-1]

    for i in range(1, m):
        for j in range(n):
            if i - 1 >= 0 and j - 1 >= 0 and pattern[i] == text[j]:
                w[i][j] = w[i-1][j-1] + w[i][j-1]
            elif j - 1 >= 0:
                w[i][j] = w[i][j-1]

    return w[m-1][n-1]



def driver_util_2(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    i = text_length - 1
    j = pattern_length - 1
    ans = [0]
    util_2(i, j, text, pattern, ans)
    return ans[0]



text = 'abcb'
pattern = 'ab'

text = 'abcabcc'
pattern = 'ac'

#
text = 'subsequence'
pattern = 'sue'

# print(function(text, pattern))
print(driver_util_2(text, pattern))
print(bottom_up(text, pattern))



