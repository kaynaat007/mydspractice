from collections import Counter
import math

def count_min(s, target_string):

    n = len(s)
    # print(target_string)
    differences = 0
    for i in range(n):
        if s[i] != target_string[i]:
            differences += 1
    # print('diff: {}'.format(differences))
    if differences % 2 != 0:
        return math.inf
    return differences//2


def get_target_string(s, base):
    target = ''
    n = len(s)
    for i in range(n):
        target += base
        if base == '0':
            base = '1'
        else:
            base = '0'
    return target


def minSwaps(s: str) -> int:

    counts = Counter(s)
    ones = counts['1']
    zeroes = counts['0']

    if abs(ones-zeroes) > 1:
        return -1

    n = len(s)

    target = get_target_string(s, '0')
    count1 = count_min(s, target)
    target = get_target_string(s, '1')
    count2 = count_min(s, target)
    return min(count1, count2)


s = '111000'
s = '010'
s = '1110'
s = '10111000'
s = '1111000'
s = '00001111'
print(minSwaps(s))

