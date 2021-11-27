

def util(i, j, text, pattern):

    if i < 0 and j < 0: # if both text and pattern is not there, return True
        return True

    if i < 0 <= j:  # if text is empty and pattern is still there , return True only if pattern is all '*'
        return len(list(filter(lambda x: x != '*', [k for k in pattern[:j+1]]))) == 0

    if j < 0 <= i: # if pattern is empty and text remains, False
        return False

    if text[i] == pattern[j] or pattern[j] == '?':
        return util(i-1, j-1, text, pattern)
    elif pattern[j] == '*':
        return util(i-1, j, text, pattern) or util(i, j-1, text, pattern)
    elif text[i] != pattern[j]:
        return False


def bottom_up(text, pattern):
    """
    bases cases:
        if text and pattern are empty
            True
        if pattern is empty and text is not empty
            False
        if text is empty and pattern is not empty
            True only if pattern is all  *
    """

    n = len(pattern)
    m = len(text)
    w = [[False for _ in range(m+1)] for _ in range(n+1)]
    w[0][0] = True # empty text and empty pattern case

    for i in range(1, n+1): # empty text and non empty pattern case
        if pattern[i-1] == '*':
            w[i][0] = w[i-1][0]
        else:
            w[i][0] = False

    # print(w)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[i-1] == '?' or pattern[i-1] == text[j-1]:
                w[i][j] = w[i-1][j-1]
            elif pattern[i-1] == '*':
                w[i][j] = w[i-1][j] or w[i][j-1]
            elif pattern[i-1] != text[j-1]:
                w[i][j] = False

    return w[n][m]

def match(text, pattern):
    m = len(pattern)
    n = len(text)
    i = n-1
    j = m-1
    return util(i, j, text, pattern)


text = 'abc'
pattern = 'a*?'

text = 'abc'
pattern = 'a******'


text = 'abc'
pattern = '????'


text = 'XYXZZXY'
pattern = 'X***Y'


text = 'XYXZZXY'
pattern = 'X***X'


text = 'XYXZZXY'
pattern = 'X***X?'

text = 'ab'
pattern = 'z*'

text = 'ab'
pattern = '**********'

text = 'abcdef'
pattern = '************'

text = 'abcdefghij'
pattern = '**************'

text = 'text'
pattern = '**????'

print(match(text, pattern))
print(bottom_up(text, pattern))
