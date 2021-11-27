from collections import defaultdict


def countHomogenous(s: str) -> int:

    if not s:
        return 0
    prime = pow(10, 9) + 7
    store = defaultdict(list)
    prev = None
    count = 0
    for ch in s:
        if prev is None or ch == prev:
            count += 1
            prev = ch
        else:
            store[prev].append(count)
            count = 1
            prev = ch
    if count != 0 and prev:
        store[prev].append(count)

    result = 0

    for key, counts in store.items():
        for count in counts:
            result = (result % prime + ((count * (count + 1))//2) % prime) % prime
    return result



s = 'abbcccaa'
s = 'xy'
s = 'zzzzz'
print(countHomogenous(s))
