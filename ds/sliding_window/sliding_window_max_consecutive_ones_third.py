"""
Learn about sliding window technique first.

we take two pointers, slow and fast.

constraint : in any window (s, f), we need to maintain at most K zeroes.

in a window the current answer at any point of time is sum of count of zero and ones.
we track those counts in c and d.

Remember we only need to slide this window if we run out of zeroes in current window to count. ( cannot exceed K )

Here we shrink the window buy how much ?
we need to shrink till we get rid of 1 extra zero.
Thats what the inner while loop is doing. Loops until it finds first zero.
we point our pointer to s + 1.
number of 1s in new window will be  total ones for the previous window  - 1s counted so far in the current window.
we set f = f + 1 ( basically increment fast pointer to move to next element.
 
"""

def consecutive_ones(a, k):
    n = len(a)
    s = 0
    f = 0
    c = 0
    d = 0
    ans = 0

    while s < n and f < n:

        if a[f] == 0:
            c += 1
        else:
            d += 1

        if c > k:
            ans = max(ans, c - 1 + d)
            dd = 0
            while s < n and a[s] == 1:
                s += 1
                dd += 1
            s = s + 1
            c = k
            d = d - dd

        f = f + 1

    ans = max(ans, c + d)
    return ans


a = [1, 1, 1, 0]
a = [1, 1, 1, 0, 1, 0, 0, 1]
# a = [0, 1, 0, 1, 0, 1, 0, 1]
a = [1,1,1,0,0,0,1,1,1,1,0]
a = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
a = [0, 0, 0]
k = 0
print(consecutive_ones(a, k))

