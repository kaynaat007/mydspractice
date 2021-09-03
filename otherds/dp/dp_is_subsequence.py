"""

on scale if you want to check weather s is a subsequence  of t, for large number of s.
think. think about t.

if s[i] and t[j] match, then
next character of s, must match with indexes greater than j in t.
why ?
because relative ordering of matched letters in t must be same as in s.
so ace is a not a  subsequence of aecddf

a matches a
c matches c
but e matches e of index less than index of last character matched which is c.


so we can have a hash of char -> list of index map of chars in t.

a --[0]
e -[1]
c --[2]
d --[3, 4]
f --[5]

once we match  a char of s into t, find index of next char in t such that it is > last index.
we can use binary search here.

"""

def is_subsequence(s, t, i, j):
    """

    """
    if i < 0 and j < 0:
        return True

    if j < 0: # if t is empty, false
        return False

    if i < 0:  # if s is empty, true since empty string is a subsequence of T.
        return True

    if s[i] == t[j]:
        return is_subsequence(s, t, i-1, j-1)
    else:
        return is_subsequence(s, t, i, j-1)

s = 'axc'
t = 'ahbgdc'

s = ''
t = ''

s = 'aabc'
t = 'abcd'

i = len(s)
j = len(t)

print(is_subsequence(s, t, i-1, j-1))
