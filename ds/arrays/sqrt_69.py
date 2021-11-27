import math

def mySqrt(x: int) -> int:

    return math.floor(math.sqrt(x))


def b_search(low, high, target, ans):

    if low > high:
        return
    mid = low + (high - low)//2
    s = mid * mid
    if s == target:
        ans[0] = mid
        return
    elif s > target:
        return b_search(low, mid-1, target, ans)
    else:
        ans[0] = mid
        return b_search(mid+1, high, target, ans)


def mySqrtV2(x: int) -> int:

     ans = [None]
     b_search(0, x, x, ans)
     return ans[0]

# x = 8
# x = 4
# x = 9
x = 16
# x = 5
# x = 12
print(mySqrt(x))
print(mySqrtV2(x))




