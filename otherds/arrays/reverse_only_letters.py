"""
i and j are pointers.
increment i and decrement j when you swap
increment i when character is non alpha
decrement j when chacracter is non alpha
"""
def reverseOnlyLetters(S: str) -> str:
    n = len(S)
    inp = list(S)
    i = 0
    j = n - 1
    while i < j:

        if not inp[i].isalpha():
            i += 1
        if not inp[j].isalpha():
            j -= 1

        if inp[i].isalpha() and inp[j].isalpha():
            v = inp[i]
            inp[i] = inp[j]
            inp[j] = v
            i += 1
            j -= 1

    return ''.join(inp)

k = 'a-bC-dEf-ghIj' #  j-Ih-gfE-dCba
k = 'ab-cd'
k = 'Test1ng-Leet=code-Q!'
k = 'a-'
k = 'a'
k = 'ab'
k = '-ab-'
# k = 'nikhil'
# k = 'abcdef'
# k = 'abc'
# k = 'proton'
k = '----'
print(reverseOnlyLetters(k))





