"""
logN approach to LIS.

observation:

extend, discard, clone technique.

we will explain with need to  maintain multiple potential LISes from observing the input array.
we will compare the element of the input array with end elements of LISes we have maintained
so far. Three conditions arise

input element:  x

if there is no LIS, create an LIS with a single element x.

if x greater than all end elements of LIS maintained, then clone the LIS which has largest
last element < x, and extend it by x.  ( clone and extend )

if x falls in between some end elements of LIS, then find an LIS whose
last element is largest and  < x. Clone this LIS, extend it by x and discard
all other LISes of same size. ( clone, extend, discard )


observe we are only comparing the new element from input array with end elements only.
so we need not maintain whole LISes. only the end elements will suffice.
Let us call the array S[]

discarding is similar to replacing. so whenever we encounter an input element x which
is less than some end element and > some other in S, we need to find the correct position for this element. This is done by binary search.

extending is same as extending S by incoming element.

why do we replace anyway ?

to give a chance of more long LIS. so say we have input [2, 5, 3, 4, 8, 9, 10, 11, 12]

say S = [2, 5]
now we have next input as 3.
how do we fit 3 ?
replacing 5 by 3 has an advantage that it there is some element like 4 upcoming next,
it can be a part of LIS. if we kept 5, 4 would be discarded.

for appraoch:

read  https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

read  https://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming

"""

from bisect import bisect_left
from datetime import datetime


def lis_nlogn(a):
    n = len(a)
    x = []
    for i in range(0, n):
        if x and a[i] > x[-1]:
            x.append(a[i])
        else:
            j = bisect_left(x, a[i])
            if len(x) == 0:
                x.append(a[i])
            else:
                x[j] = a[i]
    return x


# a = [2, 6, 3, 4, 1, 2, 9, 5, 8]
# a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
a = [1,3,6,7,9,4,10,5,6]
t = datetime.now()
x = lis_nlogn(a)
print((datetime.now() - t).total_seconds() * 1000)
print(x)
