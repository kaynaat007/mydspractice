"""
Two factors we need to esnure while constructing a new number:

"greaterness" and "smallest"


You need to find the first smaller digit from the previous digit while traversing from right side of the number.
let that digit be x.

if you can't find x, there is no answer. why ? because the give number is in the highest form. We can't make a number
greater than this number.

You need to find first digit from right which is greater than x. say d.  why ?  because this digit d will ensure the
"greaterness".  if we replace x by d, then resulting number is atleast greater than current number since
differing digit d in new number is > x in prev number.

replace d by x

Layout the scanned digits in sorted order after digit d.  why ? to guarantee that this new number is smallest possible
such number.

ans is left out n + d + digits encountered from right in sequence that contain x.

why this is correct ?

123

x = 2
d = 3
n = 1

ans = n + d + [..]
1 + 3 + 2 = 132

"""
def nextGreaterElement(n: int):

    stack = []
    ans = ""
    min_number = None
    while n:

        digit = n % 10
        n = n // 10
        if not stack or digit >= stack[-1]:
            stack.append(digit)
        else:
            min_number = digit
            break

    if min_number is None:
        return -1

    for i, e in enumerate(stack):
        if min_number < e:
            break

    v = stack[i]
    stack[i] = min_number

    ans += str(n)
    ans += str(v)
    ans += str(''.join([str(e) for e in stack]))

    ans = int(ans)

    if ans > 2147483647:
        return -1
    return ans

n = 1999999999

# n = 199

print(nextGreaterElement(n))

