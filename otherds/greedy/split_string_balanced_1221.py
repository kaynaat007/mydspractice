

def balancedStringSplit(s):
    """

    """
    n = len(s)
    if n == 0:
        return 0
    count = 0
    total_count = 0
    for e in s:
        if e == 'L':
            count += 1
        if e == 'R':
            count -= 1
        if count == 0:
            total_count += 1
    return total_count



s = 'LRRR'
s = 'RLRRLLRLRL'
s = 'RLLLLRRRLR'
s = 'LLLLRRRR'
s = 'RLRRRLLRLL'
print(balancedStringSplit(s))