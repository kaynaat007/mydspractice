
def print_matrix(k):
    print('---------')
    for i in range(len(k)):
        print(k[i])


def dp_regular_ex(S, P):
    """

    """
    n1 = len(S)
    n2 = len(P)
    re = [[False for _ in range(n1 + 1) ] for _ in range(n2 + 1)]

    re[n2][n1] = True

    j = n1
    i = n2-1
    while i >= 0:

        if i - 1 >= 0 and P[i] == '*' and (P[i-1].isalpha() or P[i-1] == '.'):
            re[i][j] = re[i+1][j]
            re[i-1][j] = re[i][j]
            i = i-2
        else:
            re[i][j] = False
            i = i - 1

    i = n1-1

    while i >= 0:
        j = n2-1
        while j >= 0:
            if j-1 >= 0 and P[j] == '*' and P[j-1].isalpha():
                alpha = P[j-1]

                if alpha == S[i]:
                    k = i
                    while k < n1 and S[k] == alpha: # last char
                        v = re[j+1][k+1] or re[j+1][k]
                        if v:
                            re[j][i] = True
                            re[j-1][i] = True
                            break
                        k = k + 1
                else:
                    re[j][i] = re[j+1][i]
                    re[j-1][i] = re[j][i]
                j = j - 2

            elif j - 1 >= 0 and P[j] == '*' and P[j-1] == '.':
                k = i + 1
                re[j][i] = False
                v1 = False
                while k <= n1:
                    v1 = re[j+1][k]
                    if v1:
                        re[j][i] = True
                        re[j-1][i] = True
                        break
                    k = k + 1

                if not v1:
                    k = i
                    re[j][i] = False
                    while k <= n1:
                        v1 = re[j + 1][k]
                        if v1:
                            re[j][i] = True
                            re[j - 1][i] = True
                            break
                        k = k + 1

                j = j - 2
            elif (0 <= i+1 <= n1 and 0 <= j+1 <= n2) and (S[i] == P[j] or P[j] == '.'):
                re[j][i] = re[j+1][i+1]
                j = j - 1
            else:
                re[j][i] = False
                j = j - 1

        i = i - 1

    # print_matrix(re)

    return re[0][0]


def recursive_regular_v2(S, P, i, j, n1, n2):
    """

    """
    print('executing for i,j as {},{}'.format(i, j))

    if i >= n1 and j >= n2: # both empty array case
        return True

    if i == -1 and j == -1:  # empty array case
        return True

    if i == -1 and j >= n2:  # empty array case
        return True

    if j + 1 < n2 and P[j] == '.' and P[j+1] == '*':  # .* case

        if i == -1:
            return recursive_regular_v2(S, P, i, j + 2, n1, n2)

        v = False
        k = i + 1
        while k <= n1:

            print('checking suffix at DOT STAR case {}, {}'.format(k, j + 2))
            v = recursive_regular_v2(S, P, k, j + 2, n1, n2)
            if v:
                break
            k = k + 1

        if v:
            print('suffix at index {} and {} matched'.format(k, j + 2))
            return True
        else:
            return False

    if j + 1 < n2 and P[j].isalpha() and P[j+1] == '*':  # [a-z]* case

        if i == -1:
            return recursive_regular_v2(S, P, i, j + 2, n1, n2)

        alpha = P[j]

        if 0 <= i < n1 and S[i] != P[j]:  # if two heads do not match, recur for remaining portion of
            # pattern P and the current char of S.
            v = recursive_regular_v2(S, P, i, j + 2, n1, n2)
            return v

        k = i
        while 0 <= k < n1 and S[k] == alpha: # iterate while you can find alpha
            k = k + 1
            print('found k at {}'.format(k)) # now alpha * job is done, recur for k, j + 2
        v = recursive_regular_v2(S, P, k, j + 2, n1, n2)
        return v

    if (0 <= i < n1 and 0 <= j < n2) and (S[i] == P[j] or P[j] == '.'):  # direct match with [a-z] or '.'
        print('char to char/dot match at index {}, {}, {}, {}'.format(i, j, S[i], P[j]))
        v = recursive_regular_v2(S, P, i+1, j+1, n1, n2)
        return v

    return False


def simple_recursive_v2(text, pattern):
    """
    if '*' is present, it would be at pattern[1].

          case 1: either entire text matches remaining pattern
          case 2: ignoring this text character at this position, remaining text matches the remaining pattern

    else:
        if pattern[0] is one of { '.', or text[0] }, recur for remaining text and pattern

    """
    if not pattern:
        return not text

    base_match = bool(text) and pattern[0] in {'.', text[0]}

    if len(pattern) >= 2 and pattern[1] == '*':
        return simple_recursive_v2(text, pattern[2:]) or (base_match and simple_recursive_v2(text[1:], pattern))
    else:
        return base_match and simple_recursive_v2(text[1:], pattern[1:])


def dp_simple_recursive_v2(text, pattern):
    """

    :param text:
    :param pattern:
    :return:
    """
    n1 = len(text)
    n2 = len(pattern)
    re = [[False  for  _ in range(n2 + 1)] for i in range(n1+1)]

    # re = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    re[n1][n2] = True
    # re[-1][-1] = True

    for i in range(n1, -1, -1):  # for each char index from reverse
        for j in range(n2 - 1, -1, -1):  # for each pattern index from reverse
            base = i < len(text) and pattern[j] in { '.', text[i]}
            if j + 1 < n2 and pattern[j + 1] == '*':
                re[i][j] = re[i][j+2] or (base and re[i+1][j])
            else:
                re[i][j] = base and re[i+1][j+1]

    # print_matrix(re)
    return re[0][0]


def isMatch(text, pattern):

    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    dp[-1][-1] = True
    for i in range(len(text), -1, -1):
        for j in range(len(pattern) - 1, -1, -1):
            first_match = i < len(text) and pattern[j] in {text[i], '.'}
            if j+1 < len(pattern) and pattern[j+1] == '*':
                dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
            else:
                dp[i][j] = first_match and dp[i+1][j+1]

    # print_matrix(dp)
    return dp[0][0]


cases = [

    {
        "input": ['ssippi', 's*p*.'],
        "output": False

    },
    {
        "input": ['aab', 'c*a*b'],
        "output": True
    },
    {
        "input": ["mississippi", "mis*is*p*."],
        "output": False
    },
    {
        'input': ['aa', 'a*'],
        'output': True
    },
    {
        'input': ['ippi', '.'],
        'output': False
    },
    {
        'input': ['aaaab', 'a*b'],
        'output': True
    },
    {
        'input': ['', 'b*'],
        'output': True
    },
    {
        'input': [ 'abc', ''],
        'output': False
    },
    {
        'input': ['', ''],
        'output': True
    },
    {
        'input': ['ab', '.*'],
        'output': True
    },
    {
        'input': [ 'aaa', '...'],
        'output': True
    },
    {
        'input': [ 'aaabaaa', '.*b.*'],
        'output': True
    },
    {
        'input': [ 'aaaab', '.*b.'],
        'output': False
    },
    {
        'input': ['abc', 'abc'],
        'output': True
    },
    {
        'input': ['aaa', 'a*a'],
        'output': True
    },
    {
        'input': ['abcd', 'd*'],
        'output': False
    },
    {
        'input': ['ab', '.*..'],
        'output': True
    },
    {
        'input': ['abbbcd', 'ab*bbbcd'],
        'output': True
    },
    {
        'input': ['aaa', 'ab*a'],
        'output': False
    }

]
#
for case in cases:
    print('running case...', case)
    i = 0
    j = 0
    S = case['input'][0]
    P = case['input'][1]
    n1 = len(S)
    n2 = len(P)
    if n1 == 0:
        i = -1
    if n2 == 0:
        j = -1
    assert case['output'] == dp_simple_recursive_v2(S, P)

print('test cases passed')

# S = cases[1]['input'][0]
# P = cases[1]['input'][1]
#
# S = 'mississippi'
# P = 'mis*is*p*.'

# S = 'ssippi'
# P = 's*p*.'

# S = 'ab'
# P = '.*'

# S = 'aaa'
# P = 'a*a'

# S = 'abcd'
# P = 'd*'

# S = 'ab'
# P = '.*..'

# S = 'bbbcd'
# P = 'b*bbbcd'

# S = "abbbcd"
# P = "ab*bbbcd"

# S = 'aab'
# P = 'c*a*b'

# S = 'ab'
# P = 'a*b'

S = 'aa'
P = 'b*a'

# S = 'a'
# P = 'a*'

# S = 'aaa'
# P = 'ab*a'
#
# S = 'aaab'
# S = 'b'
# P = 'a*b'
#
# S = 'aa'
# P = 'a*'
#
# print(dp_simple_recursive_v2(S, P))
# print(isMatch(S, P))