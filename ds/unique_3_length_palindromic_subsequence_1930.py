from collections import defaultdict


def countPalindromicSubsequence(s: str) -> int:

    """

    """

    store = defaultdict(list)
    for i, e in enumerate(s):
        store[e].append(i)

    total_count = 0
    # print(store)
    for key, val in store.items():
        first = val[0]
        last = val[-1]
        k = len(val)
        if first != last:
            unique = set()
            for i in range(first + 1, last):
                unique.add(s[i])
            total_count += len(unique)

    return total_count

s = 'aba'
s = 'aabca'
s = 'bbcbaba'
print(countPalindromicSubsequence(s))
