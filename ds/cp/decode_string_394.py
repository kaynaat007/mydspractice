def util(s, i, j):

    ans = ""
    # print('i,j', i, j)
    if i == j and s[i].isalpha():
        return s[i]

    while i <= j:
        if s[i].isdigit():
            num = s[i]
            m = i+1
            while s[m].isdigit():
                num = num + s[m]
                m += 1
            k = m
            c = 1
            while c != 0:
                k = k + 1
                if s[k] == '[':
                    c += 1  
                if s[k] == ']':
                    c -= 1
            ans = ans + int(num) * util(s, m+1, k-1)
            i = k + 1
        else:
            if s[i] != '[' or s[i] != ']':
                ans += s[i]
                i = i + 1
    return ans

def using_stack(s):

    stack = []
    n = len(s)
    if n == 0:
        return s
    k = 0
    for e in s:
        if e == '[':
            stack.append(k)
            k = 0
            stack.append('[')
        elif e.isdigit():
            k = k * 10 + int(e)
        elif e == ']':
            ans = ""
            while stack and stack[-1] != '[':
                ans = ans + stack.pop()
            stack.pop()
            ans = ans * stack[-1]
            stack.pop()
            stack.append(ans)
        else:
            stack.append(e)

    ans = ""
    for content in stack:
        ans += content[::-1]
    return ans





def decodeString(s: str) -> str:

    return util(s, 0, len(s) - 1)

s = '2[a]5[bc]'
# s = '3[a]2[bc]'
s = '3[a2[c]]'
# s = '2[abc]3[cd]ef'
# s = 'abc3[cd]xyz'
# s = '2[ab2[cd2[ef]]]d'
# s = "5[leetcode]"
print(decodeString(s))
print(using_stack(s))

