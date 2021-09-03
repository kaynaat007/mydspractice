
def count_steps(n, s, t):

    count = 0
    for i in range(n):
        if s[i] != t[i]:
            count += 1
    return count


def minOperations(s: str) -> int:

    if not s:
        return 0
    n = len(s)

    t1 = ""
    t2 = ""

    ch = "1"
    for i in range(n):
        t1 += ch
        if ch == "1":
            ch = "0"
        else:
            ch = "1"

    ch = "0"
    for i in range(n):
        t2 += ch
        if ch == "0":
            ch = "1"
        else:
            ch = "0"

    s1 = count_steps(n, s, t1)
    s2 = count_steps(n, s, t2)
    return min(s1, s2)


# s = "01"
s = "0100"
s = "10"
s = "1111"
s = "10010100"
print(minOperations(s))





