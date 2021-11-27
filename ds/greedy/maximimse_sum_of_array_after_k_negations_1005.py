

def largestSumAfterKNegations(a, k):
    """

    """
    a = sorted(a)
    n = len(a)

    if n == 0:
        return 0

    first = a[0]
    if first >= 0:
        if k % 2 == 0:
            return sum(a)
        else:
            return sum(a[1:]) - first
    else:
        s = 0
        for i, e in enumerate(a):
            if e < 0:
                k = k - 1
                s = s + -1 * e
                a[i] = -1 * e
            else:
                if k % 2 == 0:
                    return s + sum(a[i:])
                else:
                    if i - 1 >= 0:

                        if a[i] < a[i-1]:
                            a[i] = -1 * a[i]
                        else:
                            a[i-1] = -1 * a[i-1]
                        return sum(a)
                    else:
                        a[i] = -1 * a[i]
                        return sum(a)

            if k == 0:
                return s + sum(a[i+1:])

a = [4, 2, 3]
k = 2

# a = [3,-1,0,2]
# k  = 3

# a = [2,-3,-1,5,-4]
# k =  2


#
# a = [0, 0, 0]
# k = 1

# a = [5,6,9,-3,3]
# k = 2

print(largestSumAfterKNegations(a, k))


