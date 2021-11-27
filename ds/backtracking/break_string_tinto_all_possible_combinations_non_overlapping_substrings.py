
def util(s, k, n):
    if k == n:
        return [[]]

    results = []
    for i in range(k, n+1):
        left_string = s[k:i]
        if not left_string:
            continue
        output = util(s, i, n)
        for result in output:
            result.append('{' + left_string + '}')
            results.append(result)
    return results


def function(s):
    n = len(s)
    k = 0
    return util(s, k, n)

s = 'AB'
s = 'ABC'
s  = 'ABCD'
print(function(s))

