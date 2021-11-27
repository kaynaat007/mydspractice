from collections import Counter


def frequencySort(s):

    n = len(s) + 1

    bucket = [[] for _ in range(n)]

    for key, count in Counter(s).items():
            bucket[count].append(key)

    ans = ''
    for i in range(n-1, -1, -1):
        for k in bucket[i]:
            ans = ans + k * i
    return ans


def frequencySortV2(s):

    n = len(s) + 1

    bucket = [[] for _ in range(n)]

    for key, count in Counter(s).items():
            bucket[count].append(key)

    ans = ''
    for i in range(n-1, -1, -1):
        for k in bucket[i]:
            ans = ans + k * i
    return ans


s = 'cccaa'
# s = 'tree'

s = 'Aabb'

s = 'AAaaaa'
print(frequencySort(s))

