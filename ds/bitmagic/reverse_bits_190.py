
def printBits(x):

    print('bits of {}'.format(x))
    array = []

    while x:
        if x & 1:
            array.append('1')
        else:
            array.append('0')
        x = x >> 1
    return list(reversed(array))


def reverseBits(n: int) -> int:

    ans = 0
    bits = 32
    i = 32
    while i > 0:
        x = n & (1 << i) # bit at ith  position
        if x:
            ans = ans | 1 << (bits - i)
        i = i - 1
    return ans

n = 2
n = 32
# n = 5
# n = 43261596 # 964176192
# printBits(n)
n = 1 << 32
n = 43261596
ans = reverseBits(n)
b = printBits(ans)
print(b, len(b))
s = '00111001011110000010100101000000'
o = []
for ch in s:
    o.append(ch)
print(o[2:], len(o))

