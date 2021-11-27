

def util(s, i, j, n, prev_target):

    # print('{}, {}, checking for target : {}'.format(i, j, prev_target))

    if i >= n:
        return True

    for k in range(i, j, 1):
        # print('checking string {}'.format(s[i:k+1]))
        current_target = int(s[i:k+1])  # trying each substring between [i...j]
        if prev_target == current_target:
            v = util(s, k+1, j, n, current_target-1)
            if not v:
                continue
            else:
                return True
        else:
            continue
    return False


def splitString(s: str) -> bool:

    n = len(s)
    i = 0
    j = n
    for i in range(n-1):
        current_target = int(s[0:i+1])
        # print('sending {} from main'.format(current_target))
        v = util(s, i+1, j, n, current_target-1)
        if not v:
            continue
        else:
            return True
    return False


s = '10'
# s = '100000000000000000000000000000000000'
# s = '21'
s = '1234'
# s = '050043'
s = '9080701'
s = '10009998'
s = '00000000000000021'
print(splitString(s))






