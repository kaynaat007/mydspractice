
def isPowerOfThree(n: int) -> bool:

    base = 3
    if n == 1:
        return True

    while base < n:
        base = base * 3

    if base == n:
        return True
    return False

n = 1
print(isPowerOfThree(n))
